<template>
    <aside  id="aside" class="flex flex-col transition-all h-screen overflow-y-auto max-lg:fixed sticky max-lg:z-[100] max-lg:top-0 z-60 w-80 px-5 py-8 shadow-md bg-white dark:bg-gray-900 dark:border-gray-700 max-lg:-right-80">
<div class="flex  flex-col max-lg:overflow-y-auto max-lg:h-screen">

<div class="mx-auto my-2 text-center grid  ">
   

    <div class="relative text-center mx-auto  ">
        <img v-if="myuser.avatar" class="object-cover w-14 h-14 rounded-full ring ring-gray-300 dark:ring-gray-600" :src="myuser.avatar">
        <img v-else class="object-cover w-14 h-14 rounded-full ring ring-gray-300 dark:ring-gray-600" src="/assets/media/prof.png" alt="">
        <span class="h-2.5 w-2.5 rounded-full bg-emerald-500 absolute right-0 ring-1 ring-white bottom-0"></span>
 
    </div>
    
    <a v-if="myuser.current_project" href="#" style="width: 100px !important" class="text-xs bg-blue-600 p-1 w-16 text-white rounded-lg font-bold text-center mt-3 mx-auto">
    <span v-if="user.user.level==1">مدیرپروژه</span>
    <span v-else-if="user.user.level==2" style="width: auto;"> کارمند ارشد {{ user.user.rollname }} </span>
        
    <span v-else="user.user.level==2" > کارمند {{ user.user.rollname }}  </span>

    </a>
    <a v-else href="#" class="text-xs bg-blue-600 p-1 w-16 text-white rounded-lg font-bold text-center mt-3 mx-auto">نامشخص</a>

    <RouterLink  v-if="myuser.firstname"  :to="{name:'profile'}" class="text-base text-gray-700 text-center font-bold mt-1" >{{ myuser.firstname +" "   + myuser.lastname }} </RouterLink>
    <RouterLink  v-else  :to="{name:'profile'}" class="text-base text-blue-500 text-center font-bold mt-1" >تکمیل پروفایل</RouterLink>

</div>
    <div class="flex flex-col  flex-1 mt-6     
    [&amp;::-webkit-scrollbar]:w-1
    [&amp;::-webkit-scrollbar-track]:bg-gray-100
    [&amp;::-webkit-scrollbar-thumb]:bg-gray-300
    dark:[&amp;::-webkit-scrollbar-track]:bg-neutral-700
    dark:[&amp;::-webkit-scrollbar-thumb]:bg-neutral-500
    overflow-y-auto overflow-x-hidden">
        <nav class="-mx-3 space-y-3  ">
            <RouterLink :to="{name:'dashbaord'}" class="flex dashboard items-center px-3 py-3 text-blu-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700" >
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.2" stroke="#2563eb" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"></path>
                </svg>

                <span class="mx-2 text-[15px] font-medium">داشبورد</span>
            </RouterLink>
            
            <RouterLink :to="{name:'project'}" class="flex items-center px-3 py-3 text-gray-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700" >
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563eb" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 12h16.5m-16.5 3.75h16.5M3.75 19.5h16.5M5.625 4.5h12.75a1.875 1.875 0 010 3.75H5.625a1.875 1.875 0 010-3.75z"></path>
                </svg>

                <span  class="mx-2 text-[15px] font-medium">پروژه ها</span>
            </RouterLink>
            <RouterLink v-show="user.user.level==1" :to="{name:'user'}" class="flex items-center px-3 py-3 text-gray-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700" >
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563eb" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z"></path>
                </svg>

                <span class="mx-2 text-[15px] font-medium">مدیریت کاربران</span>
            </RouterLink>

            <RouterLink :to="{name:'task'}" class="flex items-center px-3 py-3 text-gray-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700" href="#">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563eb" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M10.125 2.25h-4.5c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125v-9M10.125 2.25h.375a9 9 0 019 9v.375M10.125 2.25A3.375 3.375 0 0113.5 5.625v1.5c0 .621.504 1.125 1.125 1.125h1.5a3.375 3.375 0 013.375 3.375M9 15l2.25 2.25L15 12"></path>
                </svg>

                <span  class="mx-2 text-[15px] font-medium">مدیریت تسک</span>
            </RouterLink>

            <RouterLink :to="{name:'report'}" class="flex items-center px-3 py-3 text-gray-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700" href="#">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.3" stroke="#2563eb" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3m0 0l.5 1.5m-.5-1.5h-9.5m0 0l-.5 1.5m.75-9l3-3 2.148 2.148A12.061 12.061 0 0116.5 7.605"></path>
                </svg>

                <span class="mx-2 text-[15px] font-medium">مانیتورینگ</span>
            </RouterLink>

            <RouterLink  v-show="user.user.level==1 ||  ((Sub.manager_plan=='gold' || Sub.manager_plan=='silver') && Sub.manager_plan_active)" :to="{name:'issuess'}" class="flex items-center px-3 py-3 text-gray-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700" href="#">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563eb" class="size-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 5.25h.008v.008H12v-.008Z"></path>
                  </svg>
                  
                  

                <span class="mx-2 text-[15px] font-medium">پرسش پاسخ</span>
            </RouterLink>
            <RouterLink  :to="{name:'dateTable'}" class="flex items-center px-3 py-3 text-gray-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700" href="#">
              
                <svg  xmlns="http://www.w3.org/2000/svg"
     fill="none"
    viewBox="0 0 24 24" stroke-width="1.7" stroke="#2563eb"
     class="w-6 h-6 text-gray-600">
  <path stroke-linecap="round" stroke-linejoin="round"
        d="M6.75 3v2.25M17.25 3v2.25M3.75 7.5h16.5M4.5 20.25h15a.75.75 0 00.75-.75V6.75a.75.75 0 00-.75-.75h-15a.75.75 0 00-.75.75v12.75c0 .414.336.75.75.75z" />
</svg>
                <span class="mx-2 text-[15px] font-medium">تقویم</span>
            </RouterLink>
       

            <RouterLink v-show="user.user.level==1 ||  (Sub.manager_plan=='gold' && Sub.manager_plan_active)" :to="{name:'metting'}" class="flex items-center px-3 py-3 text-gray-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700" href="#">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563eb" class="size-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M18 18.72a9.094 9.094 0 0 0 3.741-.479 3 3 0 0 0-4.682-2.72m.94 3.198.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0 1 12 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 0 1 6 18.719m12 0a5.971 5.971 0 0 0-.941-3.197m0 0A5.995 5.995 0 0 0 12 12.75a5.995 5.995 0 0 0-5.058 2.772m0 0a3 3 0 0 0-4.681 2.72 8.986 8.986 0 0 0 3.74.477m.94-3.197a5.971 5.971 0 0 0-.94 3.197M15 6.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm6 3a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Zm-13.5 0a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Z"></path>
                  </svg>
                  

                <span class="mx-2 text-[15px] font-medium">جلسه</span>
                </RouterLink>

          
        </nav>

        <div>
            <div class="flex items-center justify-between mt-8" v-show="Sub.Permissions.addprject">
                <h2 class="text-base font-semibold text-gray-800 dark:text-white">تعریف پروژه جدید</h2>

                <RouterLink :to="{name:'addproject'}" class="p-0.5 hover:bg-gray-100 duration-200 transition-colors text-gray-500 dark:border-gray-700 dark:text-gray-300 dark:hover:bg-gray-800 border rounded-lg">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563eb" class="w-4 h-4">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"></path>
                    </svg>
                </RouterLink>
            </div>

            <nav class="mt-4 -mx-3 space-y-3 ">
    

             

                <RouterLink :to="{name:'profile'}" class="flex items-center justify-between w-full px-3 py-3 text-xs font-medium text-gray-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700">
                    <span class="flex items-center gap-x-2 ">
                        <span class="w-2 h-2 bg-indigo-500 rounded-full"></span>
                        <span> پروفایل</span>
                    </span>

                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4 rtl:rotate-180">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5"></path>
                    </svg>
                </RouterLink>
           
                <RouterLink style="" :to="{name:'sub'}" class="flex items-center justify-between w-full px-3 py-3 text-xs font-medium text-gray-600 transition-colors duration-300 transform rounded-lg dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-200 hover:text-gray-700">
                    <span class="flex items-center gap-x-2 ">
                        <span class="w-2 h-2 bg-yellow-300 rounded-full"></span>
                        <span> خرید اشتراک</span>
                    </span>

                </RouterLink>
                
            </nav>
        </div>
    </div>
</div>

</aside>
</template>
<script setup>



import { onMounted, reactive, toRefs, watch } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserStore } from '@/stores/user';
import { useSubStore } from '@/stores/SubStore';
const user=useUserStore()
const Sub=useSubStore()
const myuser=reactive({
             avatar: null,
            id: null,
            email: null,
            current_project:null,
            firstname:null,
            lastname:null,
            level:null,
            rollname:''
})
const updateMyUser = () => {
    Object.assign(myuser, { ...user.user });
};

onMounted(async ()=>{
       await user.getDetail()
   updateMyUser();

       
    })
    watch(() => user.user, (newValue) => {
    updateMyUser(); 
}, { deep: true });
watch(() => user.user.current_project, (newValue) => {
    
    user.getLeveAction(user.user.current_project)
}, { deep: true });
</script>
<style>

nav a.items-center.router-link-active.dashboard{
color: #4b5563;
}
nav a.items-center.router-link-exact-active.dashboard{
color: blue;
}

.grid_res_me_right{
  right: 0 !important;
}
</style>