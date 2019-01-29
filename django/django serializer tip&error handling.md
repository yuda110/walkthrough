# Django Serializer Tip & Error Handling

### Serializer 사용 시 추가 데이터 전달

views.py에서 Serializer를 사용하려는데, 전달값으로 object 말고 추가 데이터를 넣고 싶다면, 
`context` argument를 사용한다.

    serializer = AccountSerializer(account, context={'request': request})
    serializer.data
    
이 context 값은 serialize에서 self.context로 어디에서든 가져올 수 있다.

    class SampleSerializer(serializers.ModelSerializer):
        
        def get_text(self):
            request = self.context['request']
            
_참고 [Including extra context](https://www.django-rest-framework.org/api-guide/serializers/#including-extra-context)_

---

### '...Serializer' is not JSON serializable
Serializer에서 `SerializerMethodField`를 사용할 때
  
    class SampleSerializer(serializers.ModelSerializer):
        text = serializers.SerializerMethodField()
        
        def get_text(self):
            text_qs = TextModel.objects.all()
            return TextSerializer(text_qs)
이 경우, 다음과 같은 에러가 난다.            
> 'TextSerializer' is not JSON serializable

return 값이 serialize(직렬화)되지 않았기 때문이다.
따라서 get_text()의 return 값을 다음과 같이 고쳐준다.

    def get_text(self):
                text_qs = TextModel.objects.all()
                return TextSerializer(text_qs).data
                
_참고 [Return nested serializer in serializer method field](https://stackoverflow.com/questions/33945148/return-nested-serializer-in-serializer-method-field/33945183)_