import Vue from 'vue'
import Router from 'vue-router'
import home from './views/Home.vue'
import about from './views/About.vue'
import user_home from './views/user_home.vue'
import user_q from './views/user_q.vue'
import user_info from './views/user_info.vue'
import admin_home from './views/admin_home.vue'
import admin_q_edit from './views/admin_q_edit.vue'
import admin_q from './views/admin_q.vue'

// 解决ElementUI导航栏中的vue-router在3.0版本以上重复点菜单报错问题
const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

Vue.use(Router)

export default new Router({
  mode: 'history',//去掉#
  routes: [
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/about',
      name: 'about',
      // component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
      component: about
    },
    {
      path: '/user_home',
      name: 'user_home',
      component: user_home
    },
    {
      path: '/user_info',
      name: 'user_info',
      component: user_info
    },
    {
      path: '/admin_home',
      name: 'admin_home',
      component: admin_home
    },
    {
      path: '/user_q/:id',
      name: 'user_q',
      component: user_q
    },
    {
      path: '/admin_q_edit',
      name: 'admin_q_edit',
      component: admin_q_edit
    },
    {
      path: '/admin_q/:id',
      name: 'admin_q',
      component: admin_q
    },

  ]
})
