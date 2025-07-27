<template>
    <div>
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
                <p class="text-gray-600 text-sm text-wrap">شما در این قسمت می توانید فیلدهای کاری جدیدی به پروژتان اضافه کنید</p>
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-end mx-2 mt-6 ">
              
                    <div class="flex flex-wrap ">
                        <RouterLink :to="{name:'user'}" class="flex items-center px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-orange-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z" />
                              </svg>
                              
                            <span class="mx-1 text-sm">مدیریت کاربران</span>
                        </RouterLink>
                        <RouterLink :to="{name:'skil'}" class="flex items-center mx-2 px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-green-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 0 1 2.25-2.25h7.5A2.25 2.25 0 0 1 18 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 0 0 4.5 9v.878m13.5-3A2.25 2.25 0 0 1 19.5 9v.878m0 0a2.246 2.246 0 0 0-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0 1 21 12v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6c0-.98.626-1.813 1.5-2.122" />
                              </svg>                          
                            
                            <span class="mx-1 text-sm">مدیریت فیلدها</span>
                        </RouterLink>
                    </div>
                </div>    
            </div>
           

            <section class=" w-full px-4 mx-auto ">
                <div class="flex items-center shadow-md mt-8 max-lg:mt-4 bg-white w-full max-w-3xl p-8 mx-auto lg:px-12 lg:w-3/5">
                    <div class="w-full">
                   
        
        
                        <form @submit.prevent="send" class="flex flex-col ">
                            <div class="mt-4" >
                                <label class="block mb-2 text-base text-gray-700 dark:text-gray-200">عنوان فیلد</label>
                                <input required v-model="skill.title" type="text" placeholder=" فرانت" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                            </div>
                            <div class="mt-4" >
                                <label class="block mb-2 text-base text-gray-700 dark:text-gray-200">توضیحات اختیاری</label>
                                <textarea required v-model="skill.description"  placeholder="توضیحات اختیاری" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" ></textarea>
                            </div>
                            <div class="w-full float-left " style="display: flex;flex-direction: row-reverse;">
                                <button style="font-size: 14px; margin-top: 10px;" :class="[
                                'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between  px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                loading ? ' disabled' : ''
                            ]" :disabled="loading">
                                <span>ثبت فیلد</span>
        
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
import { RouterLink } from 'vue-router';
const skill = reactive({
    title: '',
    description: '',
});
const User=useAuthStore()
import { useProjectStore } from '@/stores/project';
import { useSkillStore } from '@/stores/skil';
import { useUserStore } from '@/stores/user';
const skillstore=useSkillStore()
const loading = ref(false)
const proj=useProjectStore()
const userstore=useUserStore()
onMounted(()=>{
    if(userstore.user.level>1){
        toast.warning("شما به این صفحه دسترسی ندارید")
        router.push('/dashboard/')
    }
})
const send = async () => {
    if (!loading.value) {
        loading.value=true
        await skillstore.create({name:skill.title,description:skill.description})
        loading.value=false
   
    }

}
    </script>

    <style>
.active{
    background-color: #3b82f6;
    color: white;
}
    </style>