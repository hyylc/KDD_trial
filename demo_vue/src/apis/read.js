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

export function sign_in_admin(param){
    return service.request({
        method : "post",
        url : "/admin_sign_in",//对应flask里的路由
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


export function setq_info(param){
    return service.request({
        method : "post",
        url : "/setq_detail",//对应flask里的路由
        data:{
            setq_id : param.id
        }
    });
};

export function Perturb_One(param){
    return service.request({
        method : "post",
        url : "/perturb_one",//对应flask里的路由
        data:{
            setq_id : param.id,
            // pf : param.pf,
            ans_list : param.ans
        }
    });
};

export function Perturb_Two(param){
    return service.request({
        method : "post",
        url : "/perturb_two",//对应flask里的路由
        data:{
            setq_id : param.id,
            // pf : param.pf,
            ans_list : param.ans
        }
    });
};

export function is_existed(param){
    return service.request({
        method : "post",
        url : "/is_existed",//对应flask里的路
        data :{
            user_id : param.u_id,
            qlist : param.qlist
        }
    });
};


export function first_submit(param){
    return service.request({
        method : "post",
        url : "/new_Ans",//对应flask里的路
        data :{
            user_id : param.id_user,
            //下面三个都是列表
            qlist : param.qlist,
            ans1 : param.ans1,
            ans2 : param.ans2
        }
    });
};

export function update_submit(param){
    return service.request({
        method : "post",
        url : "/update_Ans",//对应flask里的路由
        data :{
            user_id : param.id_user,
            //下面三个都是列表
            qlist : param.qlist,
            ans1 : param.ans1,
            ans2 : param.ans2
        }
    });
};


export function Aggregate(param){
    return service.request({
        method : "post",
        url : "/project_MV_and_TD",//对应flask里的路由
        data :{
            setq_id : param.id_setq,
        }
    });
};