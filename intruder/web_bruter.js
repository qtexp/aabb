var page = require('webpage').create(),
system = require('system'),
address;



if (system.args.length ===1){
    phantom.exit(1);
}else{
    address = system.args[1];
    phantom.cookiesEnabled;
    page.open(address, function (status) {
        if (status !== 'success'){
            phantom.exit();
        }else{

            // phantom.exit();
            var cookies = page.cookies;
            var web_array = new Array();
            var web_cookies = function(){
                for(var i in cookies) {

                    var web_cookie = cookies[i].name + '=' + cookies[i].value;
                    
                }
                return web_cookie
            }

            var web_pages = page.evaluate(function(){
                return document.body.innerHTML;
                
            });
            web_array.push(web_pages);
            web_array.push(web_cookies());
            console.log(web_array);
            phantom.exit();

        }
    });
};