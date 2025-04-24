<template>
    <div v-if="!isLoading">
    <Header :info="user.user"></Header>
    
    <div id="main-content" class="row  wrapper flex parent">
    <div class="px-6 py-8 main flex flex-col w-[calc(95%-320px)] max-lg:w-full mx-auto -z-0 relative">
    <RouterView></RouterView>
    </div>
    <Aside  :user="user.user"></Aside>
    </div>
    </div>
    </template>
 

    <script setup>

    
    import { useAuthStore } from './stores/auth';
    import { getDetailuser } from './services/user';
    import { useRoute } from 'vue-router';
    import { RouterView } from 'vue-router';

    import { useUserStore } from './stores/user';
    import router from './router';
    const route=useRoute()
    const user=useUserStore()
    import Header from "./layout/Header.vue"
    import Aside from './layout/Aside.vue'
    import { onBeforeMount, onMounted, ref } from 'vue';
    const auth=useAuthStore()
    const isLoading = ref(true);

    onMounted(async ()=>{
      
       await auth.verifyAction(route.path)

       await user.getDetail()
       await user.getLeveAction(user.user.id)
      isLoading.value=false

      //  if(!user.user.isactive){
      //    router.push('/active')
      //  }
       
    })

    </script>
    
    <style>
  
    nav a.items-center.router-link-exact-active{
      color: blue ;
    }
    nav a.items-center.router-link-active{
      color: blue ;
    }
    </style>