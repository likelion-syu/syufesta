# FRONTEND 코딩 규칙 

## 1. 구조

### 1.1. 작업 파일 구조

현재 프로젝트는 크게 세가지의 앱으로 구성되어 있습니다. 

1. 공통 (common)
2. 체육대회 (competition)
3. 천보축전 (festival)

홈페이지에 모두 공통된 내용들을 가지고 있는 '공통'파트를 제외하고는 완전히 별도의 영역으로 나뉘어있습니다. 

각 프론트엔드 작업자들은 '체육대회' , '천보축전' 파트의 앱 폴더안에 있는 'templates' 폴더와 'static' 폴더를 활용하여 작업하게 됩니다. 'templates' 폴더에는 실제 HTML코드를 , 'static' 폴더에서는 각 페이지에서 필요한 css , js, image 등을 저장하여 불러오도록 합니다. 

1. 체육대회 
 - [templates](https://github.com/likelion-syu/syu-fest/tree/master/competition/templates/competition)
 - [static](https://github.com/likelion-syu/syu-fest/tree/master/competition/static/competition)

2. 천보 축전
 - [templates](https://github.com/likelion-syu/syu-fest/tree/master/festival/templates/festival)
 - [static](https://github.com/likelion-syu/syu-fest/tree/master/festival/static/festival)

데이터 처리가 필요한 페이지에서는 해당 템플릿을 render하는 views.py 함수에서 데이터를 전달 해 줄 것입니다. 필요한 데이터가 있다면 서버 개발자들에게 문의 바랍니다.

### 1.2. static 파일 사용

각 페이지에서 static 파일을 활용하는 방법은 아래와 같습니다. 현재는 common 항목을 불러오는 것을 보여주고 있습니다. 

``` 
    {% load staticfiles %}
    <!-- CSS LOAD --> 
    <!-- 실제 위치 : common/static/common/css/common.css -->
    <link type="stylesheets" href="{% static 'common/css/common.css' %}">
    
    <!-- JS LOAD -->
    <!-- 실제 위치 : common/static/common/js/likelion.module.js -->
    <script type="text/javascript" src="{% static 'common/js/likelion.module.js' %}"></script>
```

## 2. 개발 환경 및 코드 관리 

### 2.1. 개발 환경

현재 프로젝트는 모바일 화면에 최적화 되어 제작될 예정입니다. 그러므로 항상 모바일 화면을 기준으로 작업되어야 합니다. 
모바일 화면으로 개발하려면 '개발자 도구'를 활용하여 개발하여야 합니다. 되도록 크롬의 개발자 도구를 사용하여 개발하여 주시기를 부탁드립니다. [설정방법](https://jamesdreaming.tistory.com/108)은 링크를 참고하여 주세요.

### 2.2. 코드 관리

현재 코드는 4가지의 branch로 이루어져있습니다. 이는 각 작업자간의 작업이 프로젝트 전체에 미치는 영향을 최소화하고, 생산성을 높이기 위해 나누었습니다. 현재 브랜치는 아래와 같습니다.

1. master : 실제 서버에서 반영되는 브랜치입니다.
2. dev : 현재 개발 내용이 상시 반영되는 브랜치입니다. 기능이 완성되었을때 마다 master로 머지됩니다.
3. fest : 천보축전 작업자들만 사용하는 브랜치입니다. 기능이 완성되면 dev로 머지됩니다.
4. compete : 체육대회 작업자들만 사용하는 브랜치입니다. 기능이 완성되면 dev로 머지됩니다.

각 작업자는 fest , compete등의 브랜치에서만 작업하고, push 명령도 각자의 브랜치에만 해주면 됩니다. 그 이후 각 파트장의 확인 후 dev, 최종적으로 master에 합쳐지게 됩니다. 

## 3. 개발 규약 

### 3.1. templates

각 템플릿에서는 해당 템플릿을 포함하는 앱의 'base.html'을 확장하여 작성합니다. 체육대회의 경우 'competition_base.html', 축제의 경우에는 'festival_base.html'을 사용합니다. 코드는 아래와 같습니다.

``` 
    {% extends './festival_base.html' %}
    
    {% block festival-head %}
    <!-- 현재 페이지의 head 태그에 들어갈 내용 -->
    {% endblock %}

    {% block festival-content %}
    <!-- 현재 페이지의 body 태그에 들어갈 내용 -->
    {% endblock %}
``` 

#### 3.1.1. 구조

각 템플릿들은 head블록과 body블록으로 나뉘어있으니, 파일을 불러오거나 meta태그를 작성하는 경우 head블록에, 일반 html을 작성하는 경우 body 블록에 작성하면 됩니다. 

그리고 각 페이지를 작업할 때에는 현재 페이지를 모두 감싸는 'div'를 태그를 하나 작성한 후 작업을 시작해야 합니다. 

``` 
  <!-- 나쁜 예 -->
  {% block festival-content %}
    <h1>제목</h1>
    <div>
        <h3>내용</h3>
    </div>
  {% endblock %}
``` 
``` 
  <!-- 좋은 예 -->
  {% block festival-content %}
    <div class="festival-example-container">
        <h1>제목</h1>
        <div>
            <h3>내용</h3>
        </div> 
    </div>
  {% endblock %}
``` 

#### 3.1.2. 속성

특정 이벤트가 필요한 것이 아니라면 되도록 id 속성은 사용하지 않습니다. 

#### 3.1.3. 커스텀 속성

각 요소가 구분지어져야 할 값이 있다면 id가 아닌 'data-' 형태의 커스텀 속성을 작성하여 등록합니다. 아래와 같이 등록합니다.

해당 속성명은 'data-기능-값의형태'식으로 명명하도록 합니다.

``` 
<input type="button" data-btn-index="1" />
``` 

### 3.2. css

CSS 파일은 각 파일 당 하나씩 template의 이름과 동일한 css를 작성하여 사용합니다. 그리고 css의 명명은 아래와 같은 규칙을 갖습니다. 

#### 3.2.1. 클래스의 명명

되도록 스타일은 클래스를 이용하여 작성하므로 클래스명을 유의하여 작성하여야 합니다. 보통 작업 시에는 "기능을 감싸는 div" , "현재 기능의 헤더" , "현재 기능의 콘텐츠" 순으로 구조를 잡아 작업합니다. 이 경우 클래스의 이름은 '기능명-container' , '기능명-header' , '기능명-content'의 형태로 작성합니다. 

``` 
    <div class="example-container">
        <div class="example-header">
        </div>
        <div class="example-content">
        </div>
    </div>
``` 

#### 3.2.2. 클래스의 셀렉터 

위와 같은 구조를 갖는 클래스를 작성 한 경우, 클래스를 바로 셀렉트 하는 것이 아니라 템플릿을 모두 포괄하는 div를 기준으로 셀렉터를 작성합니다. 

``` 
   // 안좋은 예 
   .example-header { color : red; }

   // 괜찮은 예
   .example-container .example-header { color : red; }
``` 

