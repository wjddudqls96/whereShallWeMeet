# whereShallWeMeet🎈
만남을 책임지는 "우리 어디서 만날까?" 입니다.  

http://whereshallwemeet.shop/  
#



### 1. 프로젝트 기획 의도  

치열했던 2년동안의 코로나 전쟁이 조금은 완화되고 새로운 "위드 코로나"시대에 발 맞추어  
온라인으로만 보던 사람들을 오프라인에서도 만나고 싶다는 생각이 들었습니다.  
이에 따라, 각자의 동네 혹은 각자 알고있는 만남의 장소들을 구애받지 않고 편하게 올려 들에게 소개하고  
또 가장 많은 좋아요를 기록한 장소에서 새로운 추억을 쌓아갈 수 있는 기회를 만드는 플랫폼을 제작하고 싶었습니다.  
#
### 2. 제작 기간 & 팀원 소개  
2021년 11월 1일 ~ 2021년 11월 5일  

4인 1조 팀 프로젝트  

정영빈 : 메인페이지, 포스팅 카드, 배포  
김태우 : JWT 토큰 수정 및 파비콘 설정  
최석영 : 로그인,회원가입 페이지 및 전체 CSS   
김근형 : 포스팅 추가하기 페이지 및 영상 업로드  
#
### 3. 개발툴
Back-end  
* Python3
* Flask
* MongoDB

Front-end  
* html5
* CSS3
* JQuery
* Bulma
* deploy

Server 
* AWS EC2 (Ubuntu 18.04 LTS). 

#

### 4. 실행화면

https://user-images.githubusercontent.com/64175671/140594424-21bc5f19-ea93-4bcc-8790-f73ad4d80ac9.mp4


자세한 영상 : https://youtu.be/K7LGtKgeIMI

#
### 5. 핵심기능
#### * 로그인, 회원가입
1. JWT를 이용하여 로그인과 회원가입을 구현하였습니다.
2. 아이디와 닉네임의 중복확인이 가능합니다.

#### * 메인페이지
1. 포스팅 추가하기에서 DB에 저장한 DATA를 "GET"하여 나열합니다.
2. 반응형 CSS를 활용하여 화면 크기에 맞추어 반응합니다.

#### * 포스팅 추가하기
1. 포스팅 추가하기의 조건에 맞추어 저장합니다.
2. 각 항목중 하나라도 빠지게 되면 해당되는 알럿이 실행되며 저장이 불가합니다.
3. 주소를 입력하여 지도에 구현하였습니다.
4. 각 항목들은 DB에 "POST"합니다.

#### * 나만의 장소 페이지
1. 내가 올린 게시물들을 확인할 수 있습니다.
#
### 6. 실행 가이드
메인페이지에 접속하면 이미 들이 등록한 장소들이 보입니다.  
게시물을 보거나 올리려면 로그인이 필요합니다.  
본인의 동네 혹은 본인이 알고있는 장소들을 자랑하고 싶다면 오른쪽 상단의 로그인을 합니다.  
친구들에게 나를 알릴만한 아이디와 닉네임으로 회원가입을 하시고, 로그인을 하면 메인페이지로 돌아옵니다.  
전체 카드 박스의 오른쪽 위의 포스팅 추가하기를 눌러 나의 동네를 자랑해 보세요!  
포스팅 카드의 제목, 사진, 주소, 설명 한 가지라도 빠진다면 저장은 되지 않으니 주의가 필요합니다.  
크루원들에게 자랑할 나의 동네 혹은 나의 맛집 장소들을 크루원들에게 자랑해 보세요!  
게시물을 확인하여 좋아요 버튼을 눌러보세요.  
게시물은 왼쪽 상단의 버튼으로 최신순과 좋아요순으로 정렬이 가능합니다.  
내 게시물을 보고 싶으시다면 네비게이션바에서 나만의 장소를 확인하세요.  
화면 크기에 맞춰 반응형으로 반응합니다.  
나가실 때 로그아웃도 잊지마세요!  
  
  
친구들의 동네에서 오프라인으로 즐거운 시간 나누어요!
