<template>
<div class="">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
                <div class="bg-white relative rounded-md border border-gray-100 p-6 shadow-md shadow-black/5">
                    <div class="flex justify-between mb-6">
                        <div>
                            <div class="flex items-center mb-1">
                                <div class="text-2xl font-semibold">{{Report.detailProject.user_projects}}</div>
                            </div>
                            <div class="text-sm font-medium text-gray-400">تعداد پروژه های جاری</div>
                        </div>
                        <div class="div  shadow-slate-400 rounded-full w-[72px] h-[72px] ml-4 flex justify-center items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563EB" class="size-10">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 0 1 2.25-2.25h7.5A2.25 2.25 0 0 1 18 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 0 0 4.5 9v.878m13.5-3A2.25 2.25 0 0 1 19.5 9v.878m0 0a2.246 2.246 0 0 0-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0 1 21 12v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6c0-.98.626-1.813 1.5-2.122"></path>
                              </svg>
                              
                        </div>
                         <div class="dropdown absolute top-4 left-3">
                            <button type="button" class="dropdown-toggle text-gray-400 hover:text-gray-600">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z"></path>
                                  </svg>
                                  
                            </button>
                        
                        </div> 
                    </div>

                    <RouterLink :to="{name:'project'}" class="text-blue-500 font-medium text-sm hover:text-blue-800 " target="_blank">مشاهده </RouterLink>
                </div>
                <div class="bg-white relative rounded-md border border-gray-100 p-6 shadow-md shadow-black/5">
                    <div class="flex justify-between mb-6">
                        <div>
                            <div class="flex items-center mb-1">
                                <div class="text-2xl font-semibold">{{Report.detailProject.project_task_count}}</div>
                            </div>
                            <div class="text-sm font-medium text-gray-400">تسک های کل پروژه</div>
                        </div>
                        <div class="div  shadow-slate-400 rounded-full w-[72px] h-[72px] ml-4 flex justify-center items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#1BC700" class="size-10">
                                <path stroke-linecap="round" stroke-linejoin="round" d="m20.25 7.5-.625 10.632a2.25 2.25 0 0 1-2.247 2.118H6.622a2.25 2.25 0 0 1-2.247-2.118L3.75 7.5M10 11.25h4M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z"></path>
                              </svg>
                              
                              
                        </div>
                         <div class="dropdown absolute top-4 left-3">
                            <button type="button" class="dropdown-toggle text-gray-400 hover:text-gray-600">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z"></path>
                                  </svg>
                                  
                            </button>
                        
                        </div> 
                    </div>

                </div>
                <div class="bg-white relative rounded-md border border-gray-100 p-6 shadow-md shadow-black/5">
                    <div class="flex justify-between mb-6">
                        <div>
                            <div class="flex items-center mb-1">
                                <div class="text-2xl font-semibold">{{Report.detailProject.developers_of_project +1}}</div>
                            </div>
                            <div class="text-sm font-medium text-gray-400">تعداد کل کارمندان</div>
                        </div>
                        <div class="div  shadow-slate-400 rounded-full w-[72px] h-[72px] ml-4 flex justify-center items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokewidth="1.5" stroke="#C74600" class="size-10">
                                <path strokelinecap="round" strokelinejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z"></path>
                              </svg>
                              
                              
                              
                        </div>
                         <div class="dropdown absolute top-4 left-3">
                            <button type="button" class="dropdown-toggle text-gray-400 hover:text-gray-600">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z"></path>
                                  </svg>
                                  
                            </button>
                        
                        </div> 
                    </div>

                </div>
             
                <div class="bg-white relative rounded-md border border-gray-100 p-6 shadow-md shadow-black/5">
                    <div class="flex justify-between mb-6">
                        <div>
                            <div class="flex items-center mb-1">
                                <div class="text-2xl font-semibold">{{Report.detailProject.questions}}</div>
                            </div>
                            <div class="text-sm font-medium text-gray-400">گفت و گو ها</div>
                        </div>
                        <div class="div  shadow-slate-400 rounded-full w-[72px] h-[72px] ml-4 flex justify-center items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#8D918B" class="size-10">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.76c0 1.6 1.123 2.994 2.707 3.227 1.068.157 2.148.279 3.238.364.466.037.893.281 1.153.671L12 21l2.652-3.978c.26-.39.687-.634 1.153-.67 1.09-.086 2.17-.208 3.238-.365 1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z"></path>
                              </svg>
                              
                              
                              
                              
                        </div>
                         <div class="dropdown absolute top-4 left-3">
                            <button type="button" class="dropdown-toggle text-gray-400 hover:text-gray-600">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z"></path>
                                  </svg>
                                  
                            </button>
                        
                        </div> 
                    </div>

                    <RouterLink :to="{name:'issuess'}" class="text-blue-500 font-medium text-sm hover:text-blue-800 " target="_blank">مشاهده </RouterLink>
                </div>
            </div>

<div class="grid grid-cols-3  md:grid-cols-2 lg:grid-cols-3 gap-6 mb-2" style="  grid-template-columns: 30% 68.5%;grid-auto-rows: auto">
<div class="bg-white relative rounded-md border border-gray-100 p-6 shadow-md shadow-black/5"  >
    <div class="space-y-5">
    
        <div v-for="pr in Project.projects.data">
          <div class="mb-2 flex justify-between items-center">
            <h3 class="text-sm font-semibold text-gray-800 dark:text-white">{{ pr.title }}</h3>
            <span class="text-sm text-gray-800 dark:text-white"v-text=slicedProgress(pr.Progress)></span>
          </div>
          <div class="flex w-full h-2 bg-gray-200 rounded-full overflow-hidden dark:bg-neutral-700" role="progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
            <div :class="progressClass(pr.Progress)" :style="{ width: (pr.Progress) + '%' }"></div>
          </div>
        </div>

      
  
      </div>
</div>



  <div class="" v-if="users[0]">
    <section class="bg-white relative rounded-md border border-gray-100 p-6 shadow-md shadow-black/5" v-if="users[0]" >

            
<div class="flex flex-col">
    <div class=" -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
            <div class="overflow-hidden border border-gray-200 dark:border-gray-700 md:rounded-lg">

                <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                    <thead class="bg-gray-50 dark:bg-gray-800">
                        <tr>
                            <th scope="col" class="py-3.5 px-4 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                <button class="flex items-center gap-x-3 focus:outline-none">
                                    <span>نام </span>

                                    <svg class="h-3" viewBox="0 0 10 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M2.13347 0.0999756H2.98516L5.01902 4.79058H3.86226L3.45549 3.79907H1.63772L1.24366 4.79058H0.0996094L2.13347 0.0999756ZM2.54025 1.46012L1.96822 2.92196H3.11227L2.54025 1.46012Z" fill="currentColor" stroke="currentColor" stroke-width="0.1"></path>
                                        <path d="M0.722656 9.60832L3.09974 6.78633H0.811638V5.87109H4.35819V6.78633L2.01925 9.60832H4.43446V10.5617H0.722656V9.60832Z" fill="currentColor" stroke="currentColor" stroke-width="0.1"></path>
                                        <path d="M8.45558 7.25664V7.40664H8.60558H9.66065C9.72481 7.40664 9.74667 7.42274 9.75141 7.42691C9.75148 7.42808 9.75146 7.42993 9.75116 7.43262C9.75001 7.44265 9.74458 7.46304 9.72525 7.49314C9.72522 7.4932 9.72518 7.49326 9.72514 7.49332L7.86959 10.3529L7.86924 10.3534C7.83227 10.4109 7.79863 10.418 7.78568 10.418C7.77272 10.418 7.73908 10.4109 7.70211 10.3534L7.70177 10.3529L5.84621 7.49332C5.84617 7.49325 5.84612 7.49318 5.84608 7.49311C5.82677 7.46302 5.82135 7.44264 5.8202 7.43262C5.81989 7.42993 5.81987 7.42808 5.81994 7.42691C5.82469 7.42274 5.84655 7.40664 5.91071 7.40664H6.96578H7.11578V7.25664V0.633865C7.11578 0.42434 7.29014 0.249976 7.49967 0.249976H8.07169C8.28121 0.249976 8.45558 0.42434 8.45558 0.633865V7.25664Z" fill="currentColor" stroke="currentColor" stroke-width="0.3"></path>
                                    </svg>
                                </button>
                            </th>

                            <th scope="col" class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                نقش
                            </th>

                            <th scope="col" class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                ایمیل
                            </th>
                            <th scope="col" class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400"> آخرین بازدید</th>


                        </tr>
                    </thead>    
                    <tbody v-for="user in users" class="bg-white divide-y divide-gray-200 dark:divide-gray-700 dark:bg-gray-900">
                        <tr>
                            <td class="px-4 py-4 text-sm font-medium whitespace-nowrap">
                                <div>
                                    <h2 class="font-medium text-gray-800 dark:text-white ">
                                        <span v-if="user.first_name">{{ user.first_name+' ' }} </span>
                                        <span v-if="user.last_name"> {{ user.last_name }}</span>
                                        <span v-else>بدون نام </span>
                                    </h2>
                                    
                                </div>
                            </td>
                            <td class="px-4 py-4 text-sm font-medium whitespace-nowrap">
                                <div v-if="user.level==3" class="inline px-3 py-1 text-sm font-normal rounded-full text-emerald-500 gap-x-2 bg-emerald-100/60 dark:bg-gray-800">
                                    کاربرعادی  {{ user.skill }}
                                </div>
                                <div v-if="user.level==2" class="inline px-3 py-1 text-sm font-normal rounded-full text-emerald-500 gap-x-2 bg-emerald-100/60 dark:bg-gray-800">
                                  کاربر ارشد  {{ user.skill }}
                                </div>
                            </td>
                            <td class="px-4 py-4 text-sm whitespace-nowrap">
                                <div>
                                    <h4 class="text-gray-700 dark:text-gray-200">{{ user.email }}</h4>
                                
                                </div>
                            </td>
                            <td class="px-4 py-4 text-sm whitespace-nowrap">
                                <h4 class="text-gray-700 dark:text-gray-200" v-text="convertToJalali(user.last_login)"></h4>

                            </td>
                         
                        </tr>

                    </tbody>
                </table>

            </div>
        </div>
    </div>
</div>


</section>
        </div>
        </div>
        <div class="grid grid-cols-1  md:grid-cols-1 lg:grid-cols-1 gap-6 mb-6" style="  grid-template-columns: 100%;grid-auto-rows: auto">




  <div class="" >

    <section class=" w-full px-4 mx-auto">

            
<div class="flex flex-col mt-6">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle">
            <div class="overflow-hidden border border-gray-200 dark:border-gray-700 md:rounded-lg">

                <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                    <thead class="bg-gray-50 dark:bg-gray-800">
                        <tr>
                            <th scope="col" class="py-3.5 px-4 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                <button class="flex items-center gap-x-3 focus:outline-none">
                                    <span>عنوان</span>

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
                            <th scope="col" class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                درصد پیشرفت 
                            </th>
                         
                            <th scope="col" class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                 انجام دهنده  
                            </th>
                        
                            <th scope="col" class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">امتیاز</th>

                            <th scope="col" class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">تاریخ پایان </th>

                           
                            <th scope="col" class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">عملیات</th>

                        </tr>
                    </thead>
                    <tbody class="bg-white divide-y divide-gray-200 dark:divide-gray-700 dark:bg-gray-900">
                     
                        <tr v-for="task in taskStore.tasks">
                            <td class="px-4 py-4 text-sm font-medium whitespace-nowrap">
                                <div>
                                    <h2 class="font-medium text-gray-800 dark:text-white ">
                                        {{task.title}}

                                        <span v-if="task.importance==1" class="text-red-400">(مهم)</span>
                                        <span v-else-if="task.importance==2" class="text-red-400" style="color: chocolate;">(متوسط)</span>
                                        <span v-else class="text-red-400" style="color: green;">(کم اهمیت)</span>

                                        </h2>
                                    
                                </div>
                            </td>
                            <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                                <div v-if="!task.done" class="inline px-3 py-1 text-sm font-normal rounded-full text-blue-500 gap-x-2 bg-blue-100 dark:bg-gray-800">
                                   باز
                                </div>
                                <div v-else class="inline px-3 py-1 text-sm font-normal rounded-full bg-green-500 gap-x-2 text-white dark:bg-gray-800">
                                    بسته
                                 </div>
                            </td>
                          
                            <td class="px-4 py-4 text-sm whitespace-nowrap">
                                <div class="w-48 h-1.5 bg-blue-200 overflow-hidden rounded-full">
                                    
                                    <div v-if="task.progress" class="bg-blue-500 h-1.5" :style="{ width: task.progress + '%' }"></div>
                                    <div v-else class="bg-blue-500  h-1.5" style="width: 0;"></div>

                                </div>
                            </td>
                          
                            <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                                <span v-if="task.assigned.first_name">{{ task.assigned.first_name  }}</span> <span v-else>{{ task.assigned.email }}</span>  <span v-if="task.assigned.last_name">{{ task.assigned.last_name }}</span>

                             </td>
                           
                              <td class=" py-4 text-sm font-medium ">
                                <span class="bg-yellow-300 text-white p-2 rounded-sm" style="border-radius: 5px;" v-if="task.rate">{{ task.rate }}</span>
                                <span class="bg-yellow-300 text-white p-2 rounded-sm" style="border-radius: 5px;" v-else> بدون امتیاز</span>

                             </td>
                             <td class="px-4 py-4 text-sm font-medium whitespace-nowrap" v-text="convertToJalali(task.finished_at)">
                               
                              </td>
                         
                            <td class="px-4 py-4 text-sm whitespace-nowrap">
                         
                      
                            <RouterLink :to="{name:'singletask',params:{id:task.id}}"  style="margin: 0 5px;" class="text-sm text-white  p-2 bg-green-400 rounded-lg ">مشاهده</RouterLink>


                            </td>
                        </tr>
                    </tbody>
                </table>

            </div>
        </div>
    </div>
</div>

</section>
        </div>
        </div>
        </div>
</template>

<script setup>
const users=reactive({})
import JDate from 'jalali-date';
function convertToJalali(isoDate) {
  const date = new Date(isoDate);

  const jDate = new JDate(date);
  const jalaliYear = jDate.getFullYear();
  const jalaliMonth = jDate.getMonth(); 
  const jalaliDay = jDate.getDate();

  const hours = date.getHours();
  const minutes = date.getMinutes();
  const seconds = date.getSeconds();

  return `${jalaliYear}-${jalaliMonth.toString().padStart(2, '0')}-${jalaliDay.toString().padStart(2, '0')} ` + 
         `| ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}
import { ShowUsers } from '@/services/user';
import { useAuthStore } from '@/stores/auth';
import { useProjectStore } from '@/stores/project';
import { useReportStore } from '@/stores/Reporting';
import { useUserStore } from '@/stores/user';
import { onMounted,reactive } from 'vue';
import { useTaskStore } from '@/stores/TaskStore';
const taskStore=useTaskStore()

const User=useUserStore()
function slicedProgress(ali) {
      return String(ali).slice(0, 5) + "%";
    }

const Report=useReportStore()
const Project=useProjectStore()
const auth=useAuthStore()

onMounted(async()=>{
  Project.getprojects(auth.user.access)
  await Report.getDetail(auth.user.access,User.user.current_project)
  console.log(Report)

  ShowUsers(auth.user.access,User.user.current_project).then((data)=>{
    console.log(data)
    Object.assign(users,{...data.data})
    
}).catch((data)=>{
    
    toast.error("خطا در بارگذاری")
    router.push('/dashboard')
})

await taskStore.ShowallTaskAction()
})

function progressClass(Progress) {
               
                let baseClass = "flex flex-col justify-center rounded-full overflow-hidden text-xs text-white text-center whitespace-nowrap transition duration-500";
                if (Progress <= 25) {
                    return `${baseClass} bg-red-600`;
                } else if (Progress <= 50) {
                    return `${baseClass} bg-blue-600`;
                } else if (Progress <= 75) {
                    return `${baseClass} bg-yellow-300`;
                } else {
                    return `${baseClass} bg-green-600`;
                }
            }
           
</script>