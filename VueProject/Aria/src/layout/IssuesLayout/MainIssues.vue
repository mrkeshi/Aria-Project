<template>
    <div v-if="!isLoading">
    <div class="z-40 w-full h-full fixed top-0 right-0 backdrop-filter bg-opacity-60 bg-[#2f3c53] hidden" id="filter-overflow"></div>
    <div class="container xl:px-20 px-3 mx-auto  ">
    <Header :info="user.user"></Header>
    <RouterView></RouterView>
    </div>
</div>
</template>

<script setup>
    import Header from '@/layout/IssuesLayout/Header.vue'
    import { useAuthStore } from '@/stores/auth';
    import { getDetailuser } from '@/services/user';
    import { useRoute } from 'vue-router';
    import { RouterView } from 'vue-router';
    import { useUserStore } from '@/stores/user';
    import router from '@/router';
    const route=useRoute()
    const user=useUserStore()
    import { onBeforeMount, onMounted, ref } from 'vue';
    const auth=useAuthStore()
    const isLoading = ref(true);


    onMounted(async ()=>{
      
      await auth.verifyAction(route.path)

      await user.getDetail()
      await user.getLeveAction(user.user.id)
     isLoading.value=false

      
   })






//    my sscript Code


</script>

<style>
 .showusermanage {
  opacity: 1 !important;
  pointer-events: fill !important;
}
.ask_btn:hover>svg path{

color: blue;
}
.SiteMenu .router-link-exact-active{
      color: blue ;
    }

  
</style>
