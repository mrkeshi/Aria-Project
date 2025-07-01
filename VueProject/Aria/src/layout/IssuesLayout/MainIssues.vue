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
    import { useRoute, useRouter } from 'vue-router';
    import { RouterView } from 'vue-router';
    import { useUserStore } from '@/stores/user';
    const route=useRoute()
    const user=useUserStore()
    import { onBeforeMount, onMounted, ref } from 'vue';
    import { useToast } from 'vue-toastification';
    import { useSubStore } from '@/stores/SubStore';
    const auth=useAuthStore()
    const isLoading = ref(true);
    const toast=useToast()
    const router=useRouter()
    const subStore=useSubStore()

    onMounted(async ()=>{
    await subStore.fetchSubscriptionStatus(useAuthStore().user.access);
    if((!subStore.isActive || subStore.level<3) && (subStore.manager_plan=="free" || !subStore.manager_plan_active)){
      router.push({'name':'sub'})
        toast.info("لطفا برای دسترسی به این قسمت اشتراک خود را فعال کنید.")
    }
})
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
