<!--
 * @Date: 2020-08-25 21:34:31
 * @LastEditors: zhujian
 * @LastEditTime: 2020-08-25 21:51:24
 * @FilePath: /Novelweb/books_vue/books/src/views/Home.vue
-->
<template>
  <div class="home">
<b-container fluid>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">小说网站</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item href="#" disabled>Disabled</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="输入图书或者作者名字"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>

          <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">CN</b-dropdown-item>
            <b-dropdown-item href="#">EN</b-dropdown-item> 
          </b-nav-item-dropdown>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
      </div>
</b-container> 
<b-container  >
<div style="height:1000px;background-color:red">
body 部分 
</div>
</b-container>
<b-container fluid>
<div style="height:1000px;background-color:blue">
footer 部分 
</div>
</b-container>

</div>

</template>

<script>

export default {
  name: "Home",
  components: {
    
  }
};
</script>
