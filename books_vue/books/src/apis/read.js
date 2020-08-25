/*
 * @Date: 2020-08-25 23:53:50
 * @LastEditors: zhujian
 * @LastEditTime: 2020-08-25 23:58:52
 * @FilePath: /Novelweb/books_vue/books/src/apis/read.js
 */

import service from "../utils/request.js";


export function GetCates() {
    return service.request({
        method: "get",
        url: "/books_cates"
    });
};
