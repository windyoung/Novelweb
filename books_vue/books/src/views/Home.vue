<!--
 * @Date: 2020-08-25 21:34:31
 * @LastEditors: nobody
 * @LastEditTime: 2020-08-27 04:52:07
 * @FilePath: /Novelweb/books_vue/books/src/views/Home.vue
-->

<template>
  <div class="home">
    <Header/>
  
    <b-container>
      <div style="height:900px;background-color:red">
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
