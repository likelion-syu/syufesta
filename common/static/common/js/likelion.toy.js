(function(window){
    if(!window.__likelion){
        throw new Error("[likelion][popup] likelion 모듈이 없습니다.");
    }
    else{
        window.__likelion.ext('andefined' , function(){
            var god_eveloper = ["유경수", "배성현", "박기홍", "오지수", "위보람", "김혜원", "권택준", "김지현", "성예지", "이수연", "정현주", "이정은", "전유림", "김동혜", "Saurav"];
            let max_left = $('html').width();
            let target = $('.homelogo');
            let interval = -1;
            var count = 0;
            
            $('document').ready(function(){
                $('.homelogo').on('click' , function(){
                    count++;
                    if(count < 30 && count % 10 === 0){
                        $('.homelogo').effect('bounce');
                    }
                    else if(count === 30){
                        $('.homelogo').effect('bounce');
                        __likelion.andefined.run();
                    }
                });
            })

            let fn = {
                make : function(){
                    let item = $('<p class="driple"></p>');
                    let idx = Math.floor(Math.random()*(15));
                    let left_pos = Math.floor(Math.random()*(max_left));
                    item.text(god_eveloper[idx]);
                    item.css({
                        left : left_pos + 'px'
                    });
                    return item;
                },
                drop : function(){
                    let item = this.make();
                    $('body').append(item);
                    let duration = Math.floor(Math.random()*(2500 - 500 + 1)) + 500;
                    
                    item.animate({
                        top : '100%'
                    } , duration , function(){
                        item.remove();
                    });  
                },
                init : function(){
                    interval = setInterval(() => {
                        fn.drop();
                    }, 100);
                }
            }

            return {
                run : function(){
                    fn.init();
                }
            }
        });
    }
})(window);