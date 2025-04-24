<template>
    <div>
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
                <h1 class="text-gray-700 font-bold text-xl" >انجام دادن تسک</h1>
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-end mx-2 mt-6 ">
              
                    <div class="flex flex-wrap ">
                 
                        <RouterLink :to="{name:'task'}" class="flex items-center mx-2 px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-green-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 0 1 2.25-2.25h7.5A2.25 2.25 0 0 1 18 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 0 0 4.5 9v.878m13.5-3A2.25 2.25 0 0 1 19.5 9v.878m0 0a2.246 2.246 0 0 0-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0 1 21 12v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6c0-.98.626-1.813 1.5-2.122" />
                              </svg>                          
                            
                            <span class="mx-1 text-sm">مدیریت وظایف</span>
                        </RouterLink>
                    </div>
                </div>    
            </div>
           

            <section class=" w-full px-4 mx-auto ">
                <div class="flex items-center shadow-md mt-8 max-lg:mt-4 bg-white w-full max-w-3xl p-8 mx-auto lg:px-12 lg:w-3/5">
                    <div class="w-full">

        
                        <form @submit.prevent="send" class="flex flex-col ">
                            <h1 class="text-gray-700 mb-2 text-base dark:text-gray-300 font-bold">مشخص کردن پیشرفت تسک </h1>
                            <div class="mt-4">
                                <div class="w-full ">   
                                    
                       
                                        <label class="block mb-1 text-sm text-slate-800">
                                         درصد پیشرفت تسک 
                                        </label>
                                   
                                  
                                    <p class="flex items-center mt-2 text-xs text-slate-500">
                                 
                                    </p>
                                  </div>
                            </div>
                            <div class="mt-4" >
                                <div class="relative w-full">
                                    <div class="relative mb-6">
                                        <label for="labels-range-input" class="sr-only"> درصد پیشرفت</label>
                                        <input v-model="task.progress" id="labels-range-input" type="range" value="0" min="0" max="100" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700">
                                        <span class="text-sm text-gray-500 dark:text-gray-400 absolute start-0 -bottom-6">0 درصد</span>
                                        <span class="text-sm text-gray-500 dark:text-gray-400 absolute start-1/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6">33 درصد</span>
                                        <span class="text-sm text-gray-500 dark:text-gray-400 absolute start-2/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6">67 درصد</span>
                                        <span class="text-sm text-gray-500 dark:text-gray-400 absolute end-0 -bottom-6">100 درصد</span>
                                    </div>
                                   
                                  </div>                        
                            </div>
                      
                         
                    
                        
                                <div class="w-full mt-6">

                                    <h1 class="block mb-4  font-extrabold text-gray-900 dark:text-white" for="file_input">آپلود مستندات کاربر (اختیاری)</h1>
                                    <input  type="file" @change="handleFileUpload"
                                    class="w-full  text-gray-500 font-medium text-sm file:py-4 bg-gray-100 file:cursor-pointer cursor-pointer file:border-0  file:px-4  file:bg-gray-800 file:hover:bg-gray-700 file:text-white rounded" placeholder="s" />
                            <p class="mt-1 text-sm text-gray-500 dark:text-gray-300" id="file_input_help">لطفا در صورت نیاز مستندات لازم را آپلود نمایید.</p>
            </div>
                              
                            <div class="w-full float-left">
                                <button v-show="!loading"  style="font-size: 14px !important;margin-top: 20px;float: left;" 
                                :class="[
                                'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between  px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                loading ? ' disabled' : ''
                            ]" :disabled="loading">
                                <span> بروزرسانی </span>
        
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 rtl:-scale-x-100" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
                                </svg>
                            </button>
                            </div>
                          
                        </form>
                    </div>
                </div>
                </section>
    </div>
    </template>
    <script setup>



import { onMounted, reactive, ref } from 'vue'
import { useAuthStore } from '@/stores/auth';

const auth=useAuthStore()
const userstore=useUserStore()
import { RouterLink, useRoute } from 'vue-router';
import { useUserStore } from '@/stores/user';
import { useTaskStore } from '@/stores/TaskStore';
import { getSkils } from '@/services/skil';
import { getUserWithSkilService } from '@/services/TaskServices';
import { useToast } from 'vue-toastification';
import router from '@/router';
const route=useRoute()
const toast=useToast()
const taskStore=useTaskStore();

onMounted(async()=>{

await taskStore.SingleTaskAction(route.params.id).catch((er)=>{
    toast.error("شما به این تسک دسترسی ندارید.")
    router.push("/dashboard/tasks")
})
task.progress=taskStore.task.progress


  
});


const loading = ref(false)


const task = reactive({
      progress: 0,
  });




const send = async () => {
    
    if(task.progress>100 || task.progress<0){
        toast.warning("درصد پیشرفت پروژه نمی تواند از ۱۰۰ بیشتر یا از صفر کمتر باشد.")
    }else{
 

    task.project=userstore.user.current_project

    if (!loading.value) {
        loading.value=true

        await taskStore.updatetaskuser(task.progress,route.params.id,av)
        loading.value=false
       

    }
   
}

}


let av=null
  function handleFileUpload(event) {
    av = event.target.files[0];
  
    }


  
    </script>

    <style >
    #aside{
        height: auto !important ;
    }
.active{
    background-color: #3b82f6;
    color: white;
}
    </style>