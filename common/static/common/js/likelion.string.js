(function(window){
    if(!window.__likelion){
        throw new Error("[likelion][popup] likelion 모듈이 없습니다.");
    }
    else{
        window.__likelion.ext('str' , function(){
            // 문자열 관련 함수 추가 
            String.prototype.HAS_CHAR_IDENTIFIER = {
                SPECIAL             : 0,    // 특수문자
                NUMERIC             : 1,    // 숫자
                KOREAN              : 2,    // 한글
                ENGLISH_ALL         : 3,    // 영대소문자
                ENGLISH_SMALL_CASE  : 4,    // 영소문자
                ENGLISH_LARGE_CASE  : 5,    // 영대문자
                SPACE               : 6,    // 공백 
                NEW_LINE            : 7     // 개행문자
            }

            String.prototype.has = function () {
                if (!arguments || arguments.length === 0) { return false; }
                var _str = typeof (this) === "object" ? this.valueOf() : this;
                for (var i = 0 ; i < arguments.length; i++) {
                    var _regex;
                    switch (arguments[i]) {
                        case String.prototype.HAS_CHAR_IDENTIFIER.SPECIAL:
                            _regex = /([!\"#$%&'()*+,\-.\/:;<=>?@\[\\\]^_`{|}~])/g;
                            break;
                        case String.prototype.HAS_CHAR_IDENTIFIER.NUMERIC:
                            _regex = /([0-9])/g;
                            break;
                        case String.prototype.HAS_CHAR_IDENTIFIER.KOREAN:
                            _regex = /([ㄱ-ㅎㅏ-ㅣ가-힣])/g;
                            break;
                        case String.prototype.HAS_CHAR_IDENTIFIER.ENGLISH_ALL:
                            _regex = /([a-zA-Z])/g;
                            break;
                        case String.prototype.HAS_CHAR_IDENTIFIER.ENGLISH_SMALL_CASE:
                            _regex = /([a-z])/g;
                            break;
                        case String.prototype.HAS_CHAR_IDENTIFIER.ENGLISH_LARGE_CASE:
                            _regex = /([A-Z])/g;
                            break;
                        case String.prototype.HAS_CHAR_IDENTIFIER.SPACE:
                            _regex = /\s/g;
                            break;
                        case String.prototype.HAS_CHAR_IDENTIFIER.NEW_LINE:
                            _regex = /\r\n|\n|\r/g;
                            break;
                    }

                    if (_regex.test(_str)) { continue; }
                    else { return false; }
                }
                return true;
            }
            String.prototype.hasEng = function () { return this.valueOf().has(String.prototype.HAS_CHAR_IDENTIFIER.ENGLISH_ALL); }
            String.prototype.hasEngLarge = function () { return this.valueOf().has(String.prototype.HAS_CHAR_IDENTIFIER.ENGLISH_LARGE_CASE); }
            String.prototype.hasEngSmall = function () { return this.valueOf().has(String.prototype.HAS_CHAR_IDENTIFIER.ENGLISH_SMALL_CASE); }
            String.prototype.hasNum = function () { return this.valueOf().has(String.prototype.HAS_CHAR_IDENTIFIER.NUMERIC); }
            String.prototype.hasKor = function () { return this.valueOf().has(String.prototype.HAS_CHAR_IDENTIFIER.KOREAN); }
            String.prototype.hasSpe = function () { return this.valueOf().has(String.prototype.HAS_CHAR_IDENTIFIER.SPECIAL); }
            String.prototype.hasSpace = function () { return this.valueOf().has(String.prototype.HAS_CHAR_IDENTIFIER.SPACE); }
            String.prototype.hasNewLine = function () { return this.valueOf().has(String.prototype.HAS_CHAR_IDENTIFIER.NEW_LINE); }
            String.prototype.hasSpaceAndNewLine = function(){ return this.valueOf().has( String.prototype.HAS_CHAR_IDENTIFIER.SPACE , String.prototype.HAS_CHAR_IDENTIFIER.NEW_LINE); }
            String.prototype.trim = String.prototype.trim || function () {
                return this.valueOf().replace(/(^\s*)|(\s*$)/gi, "");
            }
        });
    }
})(window);