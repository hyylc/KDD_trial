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

export function new_setq(param){
    return service.request({
        method : "post",
        url : "/new_setQ",//对应flask里的路由
        data:{
            desc : param.desc,
            pf : param.pf,
            b : param.b
        }
    });
};

export function new_q(param){
    return service.request({
        method : "post",
        url : "/new_Q",//对应flask里的路由
        data:{
            desc : param.desc,
            setq_id : param.setq_id,
            num : param.num
        }
    });
};

export function new_option(param){
    return service.request({
        method : "post",
        url : "/new_Option",//对应flask里的路由
        data:{
            desc : param.desc,
            q_id : param.q_id,
            num : param.num
        }
    });
};