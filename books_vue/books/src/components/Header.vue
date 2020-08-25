<!--
 * @Date: 2020-08-25 22:07:21
 * @LastEditors: zhujian
 * @LastEditTime: 2020-08-25 23:45:30
 * @FilePath: /Novelweb/books_vue/books/src/components/Header.vue
-->
<template>
    <b-container fluid>
        <div>
            <b-navbar toggleable="lg" type="dark" variant="info">
                <b-navbar-brand href="#">小说网站</b-navbar-brand>
    
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    
                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav>
                        <b-nav-item href="#">Link1</b-nav-item>
                        <b-nav-item href="#">Link2</b-nav-item>
                        <b-nav-item href="#">Link3</b-nav-item>
                        <b-nav-item href="#">Link4</b-nav-item>
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
</template>


<script>
    export default {
        name: "Header",
        setup(props, context) {
            // setup 相当于 beforecreate ， created ; 
            //props:来自父组件传入的内容（来自爸爸的爱）；
            //context ：当前组件拥有的内容
        }
    }
</script>

<style lang="scss" scoped>
    // lang 解释其CSS符合什么编译器的语法 。scoped：当前vue文件生效，没有 Scoped ： 则全局生效
</style>