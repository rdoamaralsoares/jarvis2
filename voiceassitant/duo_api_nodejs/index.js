#!/usr/bin/env node

module.exports = function(context, req) {

    var data = {
        "ikey": "",
        "skey":"",
        "host":"api-xxxx.duosecurity.com"
    }

    var client = new duo_api.Client(data.ikey, data.skey, data.host);
    client.jsonApiCall(
        'POST', '/auth/v2/auth', {
            "device":"auto",
            "username":req.body.username,
            "factor":"auto"
        },
        function(res) {
            if (res.stat !== 'OK') {
                context.res = {
                    // status defaults to 200 */
                    body: {
                        'username' : req.body.username,
                        'status' : res.response.result
                    }
                };
            }
            else {
                context.res = {
                    status: 400,
                    body:  {
                        'username' : req.body.username,
                        'status' : 'failed'
                    }
                };
            }
            context.done();
    })
}