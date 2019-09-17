window.__likelion = window.__likelion || (function(){
    return {
        list : function(){
            // console.log();
        },
        ext : function(nm , fn){
            // this.prototype[nm] = fn();
            this[nm] = fn();
        }
    };
})();