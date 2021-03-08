import Vue from "vue";
import App from "./App.vue";
import 'lib-flexible';
import router from "./router";
import store from "./store";
import axios from "axios";
import VueCompositionApi from "@vue/composition-api";
import VueResource from "vue-resource";
import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import FishUI from 'fish-ui'


Vue.use(FishUI)
Vue.use(ElementUI);
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(VueCompositionApi);
Vue.use(VueResource);

Vue.config.productionTip = false;
axios.defaults.baseURL = "http://192.168.8.14:8081"



new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
