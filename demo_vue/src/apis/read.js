//请求拦截器
import service from "../utils/request.js"


export function sign_up(){
    return service.request({
        method : "post",
        url : "/user_sign_up",//对应flask里的路由
        data:{
            uname : 'lcj',
            upwd : 'lcj19961119'
        }
    });
};
