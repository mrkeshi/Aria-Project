<template>
    <div>
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
                <h1 class="text-gray-700 font-bold text-xl">دعوت کاربر به پروژه</h1>
                <p class="text-gray-600 text-sm text-wrap">شما در این قسمت می توانید کاربران جدیدی به پروژه اضافه کنید</p>
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-end mx-2 mt-6 ">
              
                    <div class="flex flex-wrap ">
                        <RouterLink :to="{name:'user'}" class="flex items-center px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-orange-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z"></path>
                              </svg>
                              
                            <span class="mx-1 text-sm">مدیریت کاربران</span>
                        </RouterLink>
                        <button class="flex items-center mx-2 px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-green-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 0 1 2.25-2.25h7.5A2.25 2.25 0 0 1 18 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 0 0 4.5 9v.878m13.5-3A2.25 2.25 0 0 1 19.5 9v.878m0 0a2.246 2.246 0 0 0-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0 1 21 12v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6c0-.98.626-1.813 1.5-2.122"></path>
                              </svg>                          
                            
                            <span class="mx-1 text-sm">مدیریت وظایف</span>
                        </button>
                    </div>
                </div>    
            </div>
           

            <section class=" w-full px-4 mx-auto ">
                <div class="flex items-center shadow-md mt-8 max-lg:mt-4 bg-white w-full max-w-3xl p-8 mx-auto lg:px-12 lg:w-3/5">
                    <div class="w-full">

        
                        <form class="flex flex-col ">
                            <div class="mt-4">
                                <h1 class="text-gray-700 mb-2 text-base dark:text-gray-300 font-bold">نوع فیلد کاربری را مشخص کنید</h1>
            
                                <div class="mt-3 md:flex md:items-center md:-mx-2">
                                    <button @click.prevent="changeRole(3)" :class="['flex justify-center  w-full px-6 py-3 text-blue-500 border border-blue-500  rounded-lg md:w-auto md:mx-2 focus:outline-none' ,  user.level == 3 ? 'active' : '']">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                        </svg>
            
                                        <span class="mx-2 text-sm">
                                            کاربر عادی
                                        </span>
                                    </button>
            
                                    <button @click.prevent="changeRole(2)" :class="['flex justify-center  w-full px-6 py-3 text-blue-500 border border-blue-500  rounded-lg md:w-auto md:mx-2 focus:outline-none' ,  user.level == 2 ? 'active' : '']">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                                        </svg>
            
                                        <span class="mx-2 text-sm">
                                            کاربر ارشد
                                        </span>
                                    </button>
                                </div>
                            </div> 
                            <div class="mt-4">
                                <label class="block mb-2 text-base text-gray-700 dark:text-gray-200">ایمیل کاربر</label>
                                <input v-model="user.email" type="email" placeholder="paressep28@gmail.com" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40">
                            </div>
                            <div class="mt-4">
                                <div class="w-full ">   
                                    
                       
                                    <label class="block mb-1 text-sm text-slate-800">
                                       حوزه کاری 
                                    </label>
                                   
                                    <div class="relative w-full">
                                      <select v-model="user.skil" class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border px-5 py-3 border-slate-200 rounded pl-3 pr-8 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-400 shadow-sm focus:shadow-md appearance-none cursor-pointer">
                                          <option value="brazil">فرنت</option>
                                          <option value="brazil">بک</option>
                                    
                                      </select>
                                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.2" stroke="currentColor" class="h-5 w-5 ml-1 absolute top-2.5 right-2.5 text-slate-700">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 15 12 18.75 15.75 15m-7.5-6L12 5.25 15.75 9"></path>
                                      </svg>
                                    </div>
                                    <p class="flex items-center mt-2 text-xs text-slate-500">
                                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5 mr-2">
                                        <path fill-rule="evenodd" d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12zm8.706-1.442c1.146-.573 2.437.463 2.126 1.706l-.709 2.836.042-.02a.75.75 0 01.67 1.34l-.04.022c-1.147.573-2.438-.463-2.127-1.706l.71-2.836-.042.02a.75.75 0 11-.671-1.34l.041-.022zM12 9a.75.75 0 100-1.5.75.75 0 000 1.5z" clip-rule="evenodd"></path>
                                      </svg>
                                      هر کاربر فقط میتواند یک فیلد شغلی داشته باشد
                                    </p>
                                  </div>
                            </div>

                            <div class="w-full float-left">
                                <button  style="font-size: 14px !important;margin-top: 20px;;" 
                                :class="[
                                'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between  px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                loading ? ' disabled' : ''
                            ]" :disabled="loading">
                                <span> دعوت کاربر</span>
        
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
import { reactive, ref } from 'vue'
import { useAuthStore } from '@/stores/auth';

const User=useAuthStore()
import { useProjectStore } from '@/stores/project';
import { RouterLink } from 'vue-router';
const loading = ref(false)
const proj=useProjectStore()
const user = reactive({
    email: '',
    skil: '',
    level:3

});
function changeRole(level){
user.level=level
}
const send = async () => {
    if (!loading.value) {
        loading.value=true
        await proj.addProject(info.title,info.description,User.user.access)
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