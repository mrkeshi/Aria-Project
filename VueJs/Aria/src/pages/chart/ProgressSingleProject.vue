<template>
           <div class="bg-white relative rounded-md border border-gray-100 p-6 shadow shadow-black/5">
                      <div class="space-y-4">
                          <h1 class="text-gray-800  font-bold">درصد پیشرفت پروژه</h1>
                          <div class="">
                            <div class="mb-2 flex justify-between items-center">
                              <h3 class="text-sm font-semibold text-gray-800 dark:text-white">{{project.single.title}}</h3>
                              <span class="text-sm text-gray-800 dark:text-white" v-text="slicedProgress(project.single.Progress)"></span>
                            </div>
                            <div class="flex w-full h-2 bg-gray-200 rounded-full overflow-hidden mb-2 dark:bg-neutral-700" role="progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
                              <div :class="progressClass(project.single.Progress)" :style="{ width: (project.single.Progress) + '%' }"></div>
                            </div>
                            <label for="" class="text-gray-500 text-sm ">{{ project.single.description }}</label>

                          </div>
                      
                    
                      
                       
                        
                  
                    
                        </div>
                  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import { useProjectStore } from '@/stores/project';
import { useUserStore } from '@/stores/user';
import { onMounted } from 'vue';
function slicedProgress(ali) {
      return String(ali).slice(0, 5) + "%";
    }
const auth=useAuthStore()
const user=useUserStore()
const project=useProjectStore()
onMounted(async()=>{
  await project.getSingle(auth.user.access,user.user.current_project)
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

<style>
</style>