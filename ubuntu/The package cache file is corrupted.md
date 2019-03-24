# The package cache file is corrupted

내 경우, 우분투에서 settings > software & Updates > Other Software
아래의 항목 몇 개를 삭제했을 때 나타난 에러였다.

    yuda@dbhost:~$ sudo apt-get update
    [sudo] password for yuda:
    Hit:1 http://kr.archive.ubuntu.com/ubuntu xenial InRelease
    Hit:2 http://kr.archive.ubuntu.com/ubuntu xenial-updates InRelease
    Hit:3 http://kr.archive.ubuntu.com/ubuntu xenial-backports InRelease
    Hit:4 http://ppa.launchpad.net/git-core/ppa/ubuntu xenial InRelease
    Hit:5 http://security.ubuntu.com/ubuntu xenial-security InRelease
    Hit:7 http://ppa.launchpad.net/notepadqq-team/notepadqq/ubuntu xenial InRelease
    Hit:8 http://ppa.launchpad.net/webupd8team/sublime-text-3/ubuntu xenial InRelease
    Get:6 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial InRelease [18.0 kB]
    Hit:9 https://packagecloud.io/slacktechnologies/slack/debian jessie InRelease
    Ign:10 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 Packages
    Ign:11 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main i386 Packages
    Ign:12 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main Translation-en
    Ign:10 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 Packages
    Ign:11 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main i386 Packages
    Ign:12 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main Translation-en
    Hit:10 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 Packages
    Err:10 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 Packages
      Hash Sum mismatch
    Hit:11 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main i386 Packages
    Hit:12 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main Translation-en
    Fetched 18.0 kB in 9s (1,915 B/s)
    Reading package lists... Error!
    E: Failed to fetch store:/var/lib/apt/lists/partial/ppa.launchpad.net_jonathonf_python-3.6_ubuntu_dists_xenial_main_binary-amd64_Packages.gz  Hash Sum mismatch
    E: Some index files failed to download. They have been ignored, or old ones used instead.
    E: Unable to parse package file /var/lib/apt/lists/ppa.launchpad.net_jonathonf_python-3.6_ubuntu_dists_xenial_main_binary-amd64_Packages (1)
    E: Unable to parse package file /var/lib/apt/lists/ppa.launchpad.net_jonathonf_python-3.6_ubuntu_dists_xenial_main_binary-i386_Packages (1)
    E: Unable to parse package file /var/lib/apt/lists/ppa.launchpad.net_jonathonf_python-3.6_ubuntu_dists_xenial_main_binary-all_Packages (1)
    E: Unable to parse package file /var/lib/apt/lists/ppa.launchpad.net_jonathonf_python-3.6_ubuntu_dists_xenial_main_i18n_Translation-en (1)
    W: You may want to run apt-get update to correct these problems
    E: The package cache file is corrupted


### 해결방법

패키지 리스트를 삭제하고 다시 업데이트를 하면 된다.

    sudo rm -rf /var/lib/apt/lists/*
    sudo apt update