/*
 * @Date: 2020-08-25 20:26:59
 * @LastEditors: zhujian
 * @LastEditTime: 2020-08-25 22:03:40
 * @FilePath: /Novelweb/books_vue/books/src/main.js
 */
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueCompositionApi from "@vue/composition-api";
import {BootstrapVue,BootstrapVueIcons} from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';


Vue.use(BootstrapVue);

Vue.use(BootstrapVueIcons);
Vue.use(VueCompositionApi);

Vue.config.productionTip = false;


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
