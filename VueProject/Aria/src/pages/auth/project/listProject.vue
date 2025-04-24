<template>
    <div>
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
                <h1 class="text-gray-700 font-bold text-xl">صفحه مدیریت پروژه ها</h1>
                <p class="text-gray-600 text-sm text-wrap">شما در این قسمت می توانید پروژه های در حال انجام و تمام شده خودد را مشاهده و مدیریت کنید.</p>
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-between mx-2 mt-6 ">
                    <div>
                        <RouterLink :to="{name:'addproject'}" class="flex items-center px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-yellow-500 max-md:my-2 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 10.5v6m3-3H9m4.06-7.19-2.12-2.12a1.5 1.5 0 0 0-1.061-.44H4.5A2.25 2.25 0 0 0 2.25 6v12a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9a2.25 2.25 0 0 0-2.25-2.25h-5.379a1.5 1.5 0 0 1-1.06-.44Z"></path>
                              </svg>
                              
                            <span class="mx-1 text-sm">تعریف پروژه جدید</span>
                        </RouterLink>
                    </div>
                    <div class="flex flex-wrap">
                  
                    </div>
                </div>    
            </div>
           

            <section class=" w-full px-4 mx-auto">

            
                <div class="flex flex-col mt-6">
                    <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
                            <div class="overflow-hidden border border-gray-200 dark:border-gray-700 md:rounded-lg">
            
                                <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                                    <thead class="bg-gray-50 dark:bg-gray-800">
                                        <tr>
                                            <th scope="col" class="py-3.5 px-4 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                                <button class="flex items-center gap-x-3 focus:outline-none">
                                                    <span>پروژه</span>
            
                                                    <svg class="h-3" viewBox="0 0 10 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                        <path d="M2.13347 0.0999756H2.98516L5.01902 4.79058H3.86226L3.45549 3.79907H1.63772L1.24366 4.79058H0.0996094L2.13347 0.0999756ZM2.54025 1.46012L1.96822 2.92196H3.11227L2.54025 1.46012Z" fill="currentColor" stroke="currentColor" stroke-width="0.1"></path>
                                                        <path d="M0.722656 9.60832L3.09974 6.78633H0.811638V5.87109H4.35819V6.78633L2.01925 9.60832H4.43446V10.5617H0.722656V9.60832Z" fill="currentColor" stroke="currentColor" stroke-width="0.1"></path>
                                                        <path d="M8.45558 7.25664V7.40664H8.60558H9.66065C9.72481 7.40664 9.74667 7.42274 9.75141 7.42691C9.75148 7.42808 9.75146 7.42993 9.75116 7.43262C9.75001 7.44265 9.74458 7.46304 9.72525 7.49314C9.72522 7.4932 9.72518 7.49326 9.72514 7.49332L7.86959 10.3529L7.86924 10.3534C7.83227 10.4109 7.79863 10.418 7.78568 10.418C7.77272 10.418 7.73908 10.4109 7.70211 10.3534L7.70177 10.3529L5.84621 7.49332C5.84617 7.49325 5.84612 7.49318 5.84608 7.49311C5.82677 7.46302 5.82135 7.44264 5.8202 7.43262C5.81989 7.42993 5.81987 7.42808 5.81994 7.42691C5.82469 7.42274 5.84655 7.40664 5.91071 7.40664H6.96578H7.11578V7.25664V0.633865C7.11578 0.42434 7.29014 0.249976 7.49967 0.249976H8.07169C8.28121 0.249976 8.45558 0.42434 8.45558 0.633865V7.25664Z" fill="currentColor" stroke="currentColor" stroke-width="0.3"></path>
                                                    </svg>
                                                </button>
                                            </th>
            
                                            <th scope="col" class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                                وضعیت
                                            </th>
            
                                            <th scope="col" class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                                توضیحات
                                            </th>
            
                                            <th scope="col" class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">تعداد کارمندان</th>
            
                                            <th scope="col" class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">درصد پیشروی</th>
            
                                            <th scope="col" class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">عملیات</th>

                                        </tr>
                                    </thead>    
                                    <tbody v-for="project in projects.projects.data" class="bg-white divide-y divide-gray-200 dark:divide-gray-700 dark:bg-gray-900">
                                        <tr>
                                            <td class="px-4 py-4 text-sm font-medium whitespace-nowrap">
                                                <div>
                                                    <h2 class="font-medium text-gray-800 dark:text-white ">{{project.title}}</h2>
                                                    
                                                </div>
                                            </td>
                                            <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                                                <div v-if="project.status" class="inline px-3 py-1 text-sm font-normal rounded-full text-emerald-500 gap-x-2 bg-emerald-100/60 dark:bg-gray-800">
                                                    تکمیل
                                                </div>
                                                <div v-else="project.status" class="inline px-3 py-1 text-sm font-normal rounded-full text-white text-emerald-500 gap-x-2 bg-orange-500 dark:bg-gray-800" style="background-color: #fbc666;">
                                                    در حال انجام
                                                </div>
                                            </td>
                                            <td class="px-4 py-4 text-sm whitespace-nowrap">
                                                <div>
                                                    <h4 class="text-gray-700 dark:text-gray-200">{{ project.description }}</h4>
                                                
                                                </div>
                                            </td>
                                            <td class="px-4 py-4 text-sm whitespace-nowrap">
                                                <div class="flex items-center">
                                                    <p class="flex items-center justify-center w-6 h-6 -mx-1 text-xs text-blue-600 bg-blue-100 border-2 border-white rounded-full">{{project.user_count}}</p>
                                                </div>
                                            </td>
            
                                            <td class="px-4 py-4 text-sm whitespace-nowrap">
                                                <div class="w-48 h-1.5 bg-blue-200 overflow-hidden rounded-full">
                                                    <div class="bg-blue-500 w-2/3 h-1.5"></div>
                                                </div>
                                            </td>
            
                                            <td class="px-4 py-4 text-sm whitespace-nowrap">
                                          
                                            <a href="#" v-if="user.user.current_project==project.id" class="text-sm text-white mx-2 p-2 bg-green-400 rounded-lg ">انتخاب شده </a>
                                            <a @click="switching(project.id)" href="#" v-else class="text-sm text-white mx-2 p-2  rounded-lg " style="background-color: #fbc666;">سوئیچ  </a>
                                            <RouterLink :to="{name:'editproject',params:{id:project.id}}" v-if="user.user.id==project.project_admin.id" class="text-sm text-white mx-2 w-auto  p-2  rounded-lg " style="background-color: blueviolet;">ویرایش</RouterLink>
                                            <a @click="deleteProject(project.id)" href="#" v-if="user.user.id==project.project_admin.id" class="text-sm text-white  p-2 bg-red-500 rounded-lg ">حذف</a>
                                            <a @click="deleteProject(project.id)" href="#" v-else="user.id==project.project_admin.id" class="text-sm text-white  p-2 bg-red-500 rounded-lg ">انصراف</a>

                                            </td>
                                        </tr>
            
                                    </tbody>
                                </table>
            
                            </div>
                        </div>
                    </div>
                </div>
            
                <!-- <div class="flex items-center justify-between mt-6">
                    <a href="#" class="flex items-center px-5 py-2 text-sm text-gray-700 capitalize transition-colors duration-200 bg-white border rounded-md gap-x-2 hover:bg-gray-100 dark:bg-gray-900 dark:text-gray-200 dark:border-gray-700 dark:hover:bg-gray-800">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 rtl:-scale-x-100">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 15.75L3 12m0 0l3.75-3.75M3 12h18"></path>
                        </svg>
            
                        <span>
                            قبلی
                        </span>
                    </a>
            
                    <div class="items-center hidden md:flex gap-x-3">
                        <a href="#" class="px-2 py-1 text-sm text-blue-500 rounded-md dark:bg-gray-800 bg-blue-100/60">1</a>
                        <a href="#" class="px-2 py-1 text-sm text-gray-500 rounded-md dark:hover:bg-gray-800 dark:text-gray-300 hover:bg-gray-100">2</a>
                        <a href="#" class="px-2 py-1 text-sm text-gray-500 rounded-md dark:hover:bg-gray-800 dark:text-gray-300 hover:bg-gray-100">3</a>
                        <a href="#" class="px-2 py-1 text-sm text-gray-500 rounded-md dark:hover:bg-gray-800 dark:text-gray-300 hover:bg-gray-100">...</a>
                        <a href="#" class="px-2 py-1 text-sm text-gray-500 rounded-md dark:hover:bg-gray-800 dark:text-gray-300 hover:bg-gray-100">12</a>
                        <a href="#" class="px-2 py-1 text-sm text-gray-500 rounded-md dark:hover:bg-gray-800 dark:text-gray-300 hover:bg-gray-100">13</a>
                        <a href="#" class="px-2 py-1 text-sm text-gray-500 rounded-md dark:hover:bg-gray-800 dark:text-gray-300 hover:bg-gray-100">14</a>
                    </div>
            
                    <a href="#" class="flex items-center px-5 py-2 text-sm text-gray-700 capitalize transition-colors duration-200 bg-white border rounded-md gap-x-2 hover:bg-gray-100 dark:bg-gray-900 dark:text-gray-200 dark:border-gray-700 dark:hover:bg-gray-800">
                        <span>
                            بعدی
                        </span>
            
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 rtl:-scale-x-100">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3"></path>
                        </svg>
                    </a>
                </div> -->
            </section>

    </div>
    </template>
    
    <script setup>
import { useUserStore } from '@/stores/user';
import { useProjectStore } from '@/stores/project';
import { onMounted, reactive, watch } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { RouterLink } from 'vue-router';
const projectsData=reactive([])
const user=useUserStore()
const auth=useAuthStore()

const projects=useProjectStore()
onMounted(async()=>{
    await projects.getprojects(auth.user.access)
    
})

async function switching(id){

    await projects.setProjCurrent(auth.user.access,id);
}
async function deleteProject(id){
await projects.deleteprojACtion(auth.user.access,user.user.current_project,id)
}
    </script>