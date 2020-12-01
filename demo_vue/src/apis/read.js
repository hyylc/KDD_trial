//请求拦截器
import service from "../utils/request.js"


export function del_user(userinfo){
    return service.request({
        method : "post",
        url : "/delete_user",//对应flask里的路由
        data:{
            user_id : userinfo
        }
    });
};
