<template>
       <section class=" dark:bg-gray-900">
                <div class="container px-6 py-6 mx-auto">
                    <h1 class="text-2xl font-semibold text-center text-gray-800 capitalize lg:text-3xl dark:text-white">برترین کاربران بر اساس تعداد تسک های انجام شده</h1>
            
                
            
                    <div class="grid grid-cols-1 gap-8 mt-8 xl:mt-12 md:grid-cols-2 xl:grid-cols-4">
                   
            
                        <div v-for="user in reporting.topuser" class="flex flex-col items-center p-6 transition-colors duration-300 transform border cursor-pointer rounded-xl hover:border-transparent group hover:bg-blue-600 dark:border-gray-700 dark:hover:border-transparent">
                            <img v-if="user.avatar" class="object-cover w-28 h-28 rounded-full ring-4 ring-gray-300" :src="user.avatar" alt="">

                            <img v-else class="object-cover w-28 h-28 rounded-full ring-4 ring-gray-300" src="/assets/media/ue.jpg" alt="">
            
                            <h1 v-if="user.first_name" class="mt-4 text-xl font-semibold text-gray-700 capitalize dark:text-white group-hover:text-white">{{user.first_name+" "+user.last_name}}</h1>
                            <h1 v-else class="mt-4 text-xl font-semibold text-gray-700 capitalize dark:text-white group-hover:text-white">{{user.email}}</h1>


            
                            <div class="flex mt-3 -mx-2">
                             
                                <a  href="#" class="  dark:text-gray-300 text-[16px] p-2 rounded-md bg-[#f3f3f3] text-blue-500 border border-blue-500  dark:hover:text-gray-300 group-hover:text-blue-500 group-hover:bg-white" aria-label="Facebook">
                             <span v-if="user.average_score_for_tasks" v-text="slicedProgress(user.average_score_for_tasks)"> </span>
                             <span v-else> میانگین امتیاز :0</span>  
                                   </a>
                                <a href="#" class="mx-2  dark:text-gray-300 text-[16px] p-2 rounded-md bg-blue-600 text-white hover:text-gray-500 dark:hover:text-gray-300 group-hover:text-blue-500 group-hover:bg-white" aria-label="Facebook">
                                  {{user.count_of_task_user_completed}} تسک  کامل
                                </a>
                                
                            
                            </div>
                        </div>
                   
                    </div>
                </div>
            </section>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import { useReportStore } from '@/stores/Reporting';
import { useUserStore } from '@/stores/user';
import { onMounted } from 'vue';
function slicedProgress(ali) {
      return "میانگین امتیاز :"+String(ali).slice(0, 5) + "";
    }
const user=useUserStore()
const reporting=useReportStore()
const auth=useAuthStore()
onMounted(async()=>{
    await reporting.getTopUser(auth.user.access,user.user.current_project)
})
</script>

<style>

</style>