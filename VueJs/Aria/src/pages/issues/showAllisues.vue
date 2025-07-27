<template>

<div>

    
    <section>
            <div class="row flex mt-12 max-lg:mt-8 justify-between w-full px-2 py-6 items-center max-lg:felx-col  max-lg:flex-wrap ">
                    <div class="flex items-center max-lg:hidden ">
                                <img class="h-28 max-lg:h-20" src="/assets/media/ask_answer.png" alt="">
                                <h2 class="text-3xl font-bold text-gray-600 max-lg:text-xl">پرسش و پاسخ ها</h2>
                            </div>
<div class="flex max-lg:flex-wrap items-center max-lg:felx-col">
  <RouterLink :to="{name:'addissuess'}" class="h-16 mx-2 max-lg:w-full max-lg:justify-center max-lg:text-center ask_btn bg-blue-500 px-4 py-1 w-auto flex rounded-lg text-white items-center text-[18px] border-2 border-blue-500 hover:bg-[#f3f3f3] hover:text-blue-500  max-lg:text-md">
                                ثبت پرسش جدید
                                <svg class="mr-2" width="39" height="39" viewBox="0 0 42 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path class="stroke-current text-white transition duration-200 dark:group-hover:text-blue-450 group-hover:text-blue-700" d="M16.293 20.7224H21.0723M25.8517 20.7224H21.0723M21.0723 20.7224V15.943V25.5017" stroke-width="2.53025" stroke-linecap="round" stroke-linejoin="round"></path>
                                    <path class="stroke-current text-white transition duration-200 dark:group-hover:text-blue-450 group-hover:text-blue-700" opacity="0.5" d="M7.9995 20.7225C7.9995 23.6454 8.15777 25.908 8.54928 27.6696C8.93759 29.4168 9.53832 30.5928 10.3702 31.4247C11.2021 32.2566 12.3781 32.8573 14.1253 33.2456C15.887 33.6372 18.1495 33.7954 21.0725 33.7954C23.9954 33.7954 26.2579 33.6372 28.0196 33.2456C29.7668 32.8573 30.9428 32.2566 31.7747 31.4247C32.6066 30.5928 33.2073 29.4168 33.5956 27.6696C33.9871 25.908 34.1454 23.6454 34.1454 20.7225C34.1454 17.7995 33.9871 15.537 33.5956 13.7754C33.2073 12.0281 32.6066 10.8521 31.7747 10.0202C30.9428 9.18833 29.7668 8.58759 28.0196 8.19928C26.2579 7.80778 23.9954 7.64951 21.0725 7.64951C18.1495 7.64951 15.887 7.80778 14.1253 8.19928C12.3781 8.58759 11.2021 9.18833 10.3702 10.0202C9.53832 10.8521 8.93759 12.0281 8.54928 13.7754C8.15777 15.537 7.9995 17.7995 7.9995 20.7225Z" stroke-width="2.53025" stroke-linecap="round" stroke-linejoin="round">
                                    </path>
                                </svg>
                            </RouterLink>
  <button  v-if="tog" style="background-color: orange" @click="setFilter"  class="h-16 mx-2 my-2 max-lg:mx-2 max-lg:w-full max-lg:justify-center max-lg:text-center ask_btn bg-blue-500 px-4 py-1 w-auto flex rounded-lg text-white items-center text-[18px] hover:bg-[#f3f3f3]   max-lg:text-md">
                                فیلتر پرسش های من
            </button>
            <button  v-else style="background-color: orange" @click="setFilter"  class="h-16 mx-2 my-2 max-lg:mx-2 max-lg:w-full max-lg:justify-center max-lg:text-center ask_btn bg-blue-500 px-4 py-1 w-auto flex rounded-lg text-white items-center text-[18px] hover:bg-[#f3f3f3]   max-lg:text-md">
                               حذف فیلتر
            </button>
</div>
                       
                           
            </div>
           
        </section>
        
        <section>
            <div class="row my-4 max-lg:mt-4  w-[90%] flex flex-col  mx-auto justify-center max-lg:w-full max-lg:px-4">
            
                <div v-if="IssuesStore.allIssues[0]" v-for="qs in IssuesStore.allIssues" class="questions w-full shadow-sm bg-white rounded-2xl mt-6 ">
                        <div class="header w-full justify-between p-8 max-lg:p-4 flex items-center ">
                                <div class="flex flex-row items-center">
                                    <img v-if="qs.creator_avatar" :src="qs.creator_avatar"  style="width: 72px;" class="h-[72px] max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-gray-300" alt="">

                                            <img v-else src="/assets/media/prof.png" style="width: 72px;" class="h-[72px] max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-gray-300" alt="">
                                            <div>
                                                <h3 class="text-gray-600 text-[22px] max-lg:text-[18px] font-bold">{{ qs.creator_name }}</h3>
                                                
                                                <RouterLink
  :to="{ name: 'singleissuess', params: { id: qs.id } }"
  href="#"
  class="text-blue-400 text-sm"
  v-text="humanReadableTimeAgo(
    getLatestUpdate(qs)
  ) + ' آپدیت شد.'"
/>
                                            </div>
                                        </div>
                               
                                <div class="flex">
                                    <RouterLink :to="{name:'singleissuess',params:{id:qs.id}}" href="" style="width: auto;" class="flex items-center transition hover:bg-gray-500 hover:text-white rounded-lg bg-gray-200 w-[108px] max-lg:text-sm max-lg:w-28 text-gray-500 p-2.5 px-2 text-center pr-3.5 ">
                                        <svg class="" width="21" height="20" viewBox="0 0 21 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path stroke="currentColor" d="M8.12134 11.7807L4.13281 7.7599L8.12134 3.73914" stroke-width="1.48905" stroke-linecap="round" stroke-linejoin="round"></path>
                                            <path stroke="currentColor" d="M16.8961 16.6058V10.9767C16.8961 10.1236 16.5599 9.30549 15.9615 8.70226C15.3631 8.09902 14.5515 7.76013 13.7053 7.76013H4.13281" stroke-width="1.48905" stroke-linecap="round" stroke-linejoin="round"></path>
                                        </svg>
                                      <span v-if="melength(qs.answers)>0" >{{ melength(qs.answers) + " پاسخ " }}</span>
                                      <span v-else>بدون پاسخ </span>
                                    </RouterLink>
                                    
                                      <a  v-if="qs.status==1" style="background-color: cornflowerblue;" class=" mx-2 px-6 text-white p-2 rounded-md">باز</a>
                                      <a  v-else style="background-color: #22c55e;" class=" mx-2 px-6 text-white p-2 rounded-md">بسته</a>

                                </div>
                        </div>
                        <div class="-mt-3 px-8 justify-center item max-lg:px-4 flex-col max-lg:mt-2 ">
                            <RouterLink :to="{name:'singleissuess',params:{id:qs.id}}" class="text-gray-600 mb-2 font-bold text-[26px] px-2 transition hover:text-blue-500 max-lg:text-xl">{{ qs.subject }}</RouterLink>
                            <p style="line-height: 35px;" class="main-c max-lg:text-[14px] text-[16px] px-2  text-gray-500" v-text="truncate(qs.description)">
                            </p>
                        </div>
                      <div class="mb-3 max-lg:my-4 p-8 max-lg:p-4 py-2 flex justify-end ">

                        <label class="border border-blue-500  text-blue-500  hover:text-white hover:bg-blue-600  rounded ml-2 p-2 " v-if="qs.task" v-text="qs.task_name"></label>
                        <label class="transition border border-purple-600 text-purple-500  hover:text-white hover:bg-purple-600 rounded ml-2 p-2 " v-if="qs.task" v-text="qs.task_importance"></label>

                        <label class="transition border border-yellow-500  text-yellow-500  hover:text-white hover:bg-yellow-500 rounded ml-2 p-2 " v-if="qs.user_role.level!=1" v-text="qs.user_role.skill_name">  </label>

                      </div>
                      <div v-if="user.user.level==1 || user.user.id==qs.creator" class="border-t mt-3 border-gray-200 p-8 flex justify-end">
               <RouterLink v-if="user.user.id==qs.creator" :to="{name:'editissuess',params:{id:qs.id}}" href="#" class="text-sm mx-3 text-orange-400">ویرایش</RouterLink>
               <a style="cursor: pointer;" @click="deleteTask(qs.id)" class="text-sm mx-3 text-red-400">حذف</a>

                             </div>
                </div>
                <div v-else>
                        <h2>هیچ چیزی برای نمایش وجود ندارد</h2>
                </div>
            </div>
        </section>
</div>

</template>

<script setup>
import humanReadableTimeAgo from '@/utils/dateLog';
import { useIssuesStore } from '@/stores/IssuesStore';
import { useUserStore } from '@/stores/user';
import { onMounted,computed, ref  } from 'vue';
import { RouterLink } from 'vue-router';
import swswalDel from "@/utils/swal.js"
const IssuesStore=useIssuesStore()
const user=useUserStore()
const tog=ref(true)
const truncate = (text) => {
      return text.length > 100 ? text.substring(0, 100) + '...' : text;
    };

onMounted(async()=>{
  
  await  IssuesStore.getAllIssues(user.user.current_project)
})
function melength(x){
    if(x[0]){

   
    return x.length
}
return 0
}

async function deleteTask(id){
  await  swswalDel().then((res)=>{
    if (res.isConfirmed){
         IssuesStore.deleteIssues(id,user.user.current_project).then((res)=>{})
    }
  })

}
function getLatestUpdate(qs) {
    if (qs.answers && qs.answers.length > 0) {
      const lastAnswerDate = qs.answers[qs.answers.length - 1].updated_at;
      const questionUpdateDate = qs.updated_at;
      
      return lastAnswerDate > questionUpdateDate ? lastAnswerDate : questionUpdateDate;
    } else {
      return qs.updated_at;
    }
    }
  
  async function setFilter(){
    if(tog.value==true){

    
    await IssuesStore.getMyIssues(user.user.current_project,user.user.id)
    
      tog.value=false
  }else{
    await  IssuesStore.getAllIssues(user.user.current_project)

      tog.value=true
    }
  }
</script>

<style>

</style>