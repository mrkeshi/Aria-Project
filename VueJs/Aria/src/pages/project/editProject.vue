<template>
    <div>
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
                <h1 class="text-gray-700 font-bold text-xl" > ویرایش پروژه</h1>
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-end mx-2 mt-6 ">
              
                    <div class="flex flex-wrap ">
                      
                        <RouterLink :to="{name:'project'}"  class="flex items-center mx-2 px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-yellow-500 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 0 1 2.25-2.25h7.5A2.25 2.25 0 0 1 18 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 0 0 4.5 9v.878m13.5-3A2.25 2.25 0 0 1 19.5 9v.878m0 0a2.246 2.246 0 0 0-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0 1 21 12v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6c0-.98.626-1.813 1.5-2.122" />
                              </svg>                          
                            
                            <span class="mx-1 text-sm">مدیریت پروژه ها</span>
                        </RouterLink>
                    </div>
                </div>    
            </div>
           

            <section class=" w-full px-4 mx-auto ">
                <div class="flex items-center shadow-md mt-8 max-lg:mt-4 bg-white w-full max-w-3xl p-8 mx-auto lg:px-12 lg:w-3/5">
                    <div class="w-full">
                   
        
        
                        <form @submit.prevent="send" class="flex flex-col ">
                            <div class="mt-4" >
                                <label class="block mb-2 text-base text-gray-700 dark:text-gray-200">عنوان پروژه</label>
                                <input required v-model="info.title" type="text" placeholder="مثلا پروژه مدیریت کاربران" class="block w-full px-5 py-3 mt-2 text-sm text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                            </div>
                            <div class="mt-4" >
                                <label  class="block mb-2 text-base text-gray-700 dark:text-gray-200">توضیحات پروژه</label>
                               
                                    <textarea required  v-model="info.description" class="block w-full px-5 py-3 mt-2 text-gray-700 text-sm placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" rows="5" placeholder="لطفا توضیحات پروژه را در این قسمت وارد کنید."></textarea>
                          
                            </div>


                            <div class="w-full float-left flex " style="flex-direction: row-reverse;">
                                <button style="font-size: 14px !important;margin-top: 20px;;" 
                                :class="[
                                'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between  px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                loading ? ' disabled' : ''
                            ]" :disabled="loading">
                                <span>ویرایش پروژه</span>
        
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 rtl:-scale-x-100" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd"
                                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                        clip-rule="evenodd" />
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
import { useRoute } from 'vue-router';
const route=useRoute()
const User=useAuthStore()
import { useProjectStore } from '@/stores/project';
import { jsx } from 'vue/jsx-runtime';
const loading = ref(false)
const proj=useProjectStore()
const info = reactive({
    title: '',
    description: '',

});
onMounted(async()=>{
await proj.getSingle(User.user.access,route.params.id)

info.title=proj.single.title
  info.description=proj.single.description
})
const send = async () => {
    if (!loading.value) {
        loading.value=true
        await proj.editProject(info.title,info.description,User.user.access,route.params.id)
        loading.value=false
   
    }

}
    </script>