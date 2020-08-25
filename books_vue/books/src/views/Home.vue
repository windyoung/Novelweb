<!--
 * @Date: 2020-08-25 21:34:31
 * @LastEditors: zhujian
 * @LastEditTime: 2020-08-26 06:52:08
 * @FilePath: /Novelweb/books_vue/books/src/views/Home.vue
-->
<template>
  <div class="home">
    <Header/>
    <b-container>
      <div style="height:1000px;background-color:red">
        body 部分
      </div>
    </b-container>
    <Footer />
  </div>
</template>

<script>
  import Header from "../components/Header.vue"
  import Footer from "../components/Footer.vue"
  
  export default {
    name: "Home",
    components: {
      Header,
      Footer
    }
  };
</script>
