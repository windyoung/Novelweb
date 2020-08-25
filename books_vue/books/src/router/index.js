/*
 * @Date: 2020-08-25 21:50:23
 * @LastEditors: zhujian
 * @LastEditTime: 2020-08-25 22:04:51
 * @FilePath: /Novelweb/books_vue/books/src/router/index.js
 */
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {//网站首页
    path: "/",
    name: "Home",
    component: Home
  },
  //网站分类页
  //图书首页
  //图书详情页
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
