//请求拦截器
import service from "../utils/request.js"


export function sign_up(param){
    return service.request({
        method : "post",
        url : "/user_sign_up",//对应flask里的路由
        data:{
            uname : param.username,
            upwd : param.password
        }
    });
};

export function sign_in(param){
    return service.request({
        method : "post",
        url : "/user_sign_in",//对应flask里的路由
        data:{
            uname : param.username,
            upwd : param.password
        }
    });
};

export function get_all_setq(){
    return service.request({
        method : "post",
        url : "/all_setq",//对应flask里的路由
        data:{
        }
    });
};