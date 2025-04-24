<template>
<div id="filter" class="filter bg-black opacity-45 h-screen w-screen fixed z-50 hidden"></div>
<header>
    <nav class="relative bg-white shadow dark:bg-gray-800 z-10">
        <div class=" px-6 py-4 max-lg:px-3  mx-auto">
            <div class="flex items-center justify-between">
                <div class="flex items-center justify-between">
                    
                    <a v-if="projectname" href="#" class="text-blue-700 text-2xl font-bold max-lg:text-xl">
                    پروژه  : {{projectname}} 
                    </a>
                    <a v-else href="#" class="text-blue-700 text-2xl font-bold max-lg:text-xl">
                     بدون پروژه
                    </a>
                  
                </div>
    
                <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
                <div x-cloak="" class=" inset-x-0 z-20  w-auto transition-all duration-300 ease-in-out bg-white dark:bg-gray-800 lg:mt-0 lg:p-0 lg:top-0 lg:relative lg:bg-transparent lg:w-auto lg:opacity-100 lg:translate-x-0 lg:flex lg:items-center">
               
    
                    <div class="flex items-center ">
                        <button class="flex mx-4 text-black transition-colors duration-300 transform lg:block dark:text-gray-200 hover:text-gray-700 dark:hover:text-gray-400 focus:text-gray-700 dark:focus:text-gray-400 focus:outline-none" aria-label="show notifications">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M10.343 3.94c.09-.542.56-.94 1.11-.94h1.093c.55 0 1.02.398 1.11.94l.149.894c.07.424.384.764.78.93.398.164.855.142 1.205-.108l.737-.527a1.125 1.125 0 0 1 1.45.12l.773.774c.39.389.44 1.002.12 1.45l-.527.737c-.25.35-.272.806-.107 1.204.165.397.505.71.93.78l.893.15c.543.09.94.559.94 1.109v1.094c0 .55-.397 1.02-.94 1.11l-.894.149c-.424.07-.764.383-.929.78-.165.398-.143.854.107 1.204l.527.738c.32.447.269 1.06-.12 1.45l-.774.773a1.125 1.125 0 0 1-1.449.12l-.738-.527c-.35-.25-.806-.272-1.203-.107-.398.165-.71.505-.781.929l-.149.894c-.09.542-.56.94-1.11.94h-1.094c-.55 0-1.019-.398-1.11-.94l-.148-.894c-.071-.424-.384-.764-.781-.93-.398-.164-.854-.142-1.204.108l-.738.527c-.447.32-1.06.269-1.45-.12l-.773-.774a1.125 1.125 0 0 1-.12-1.45l.527-.737c.25-.35.272-.806.108-1.204-.165-.397-.506-.71-.93-.78l-.894-.15c-.542-.09-.94-.56-.94-1.109v-1.094c0-.55.398-1.02.94-1.11l.894-.149c.424-.07.765-.383.93-.78.165-.398.143-.854-.108-1.204l-.526-.738a1.125 1.125 0 0 1 .12-1.45l.773-.773a1.125 1.125 0 0 1 1.45-.12l.737.527c.35.25.807.272 1.204.107.397-.165.71-.505.78-.929l.15-.894Z"></path>
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"></path>
                              </svg>
                              
                        </button>
    
                        <button @click="logoutEvent" type="button" class="flex text-red-600 items-center focus:outline-none" aria-label="toggle profile dropdown">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15m-3 0-3-3m0 0 3-3m-3 3H15"></path>
                              </svg>
                              
    
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</header>
<div onclick="toggle()" class="bg-blue-500 text-white lg:hidden p-3 rounded-full cursor-pointer fixed left-4 bottom-4 z-[2000]">

            
<svg id="open" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#fff" class="size-6">
    <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 5.25h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5"></path>
  </svg>
  <svg class="hidden size-6" id="close" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokewidth="{1.5}" stroke="#fff">
    <path strokelinecap="round" strokelinejoin="round" d="M6 18 18 6M6 6l12 12"></path>
  </svg>
  
</div>
</template>

<script setup>
import { singleProject } from '@/services/projects';
import { useAuthStore } from '@/stores/auth';
import { useUserStore } from '@/stores/user';
import { onMounted, ref, watch } from 'vue';
const projectname=ref(null)

async function getprojectName(){
  if (user.user.current_project != null) {
     
     await singleProject(auth.user.access,user.user.current_project).then((response)=>{
           console.log("RESPPONSE",response.data.title)
       projectname.value=response.data.title
     });
   } 
       else {
     projectname.value = null;
   }
}
onMounted(async ()=>{
  getprojectName()
})

const user=useUserStore()
const auth=useAuthStore()
function logoutEvent(){
    auth.logoutAction()
}

watch(
  async () => user.user.current_project, 
  async (newValue) => {  

    if (user.user.current_project != null) {

      await singleProject(auth.user.access,user.user.current_project).then((response)=>{
      
        projectname.value=response.data.title
      
      });
    } else {
      projectname.value = null;
    }

  },
  { deep: true }
);
watch(
  async () => user.projectname, 
  async (newValue) => {  

    if (user.user.current_project != null) {

      await singleProject(auth.user.access,user.user.current_project).then((response)=>{
      
        projectname.value=response.data.title
      
      });
    } else {
      projectname.value = null;
    }

  },
  { deep: true }
);
</script>