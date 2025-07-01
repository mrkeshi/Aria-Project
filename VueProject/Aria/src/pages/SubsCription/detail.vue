<template>
           <div class="w-full py-10 px-4 " >
                <div class="max-w-7xl mx-auto space-y-6" >
              
                  <div class="shadow rounded-xl p-6 flex flex-col sm:flex-row sm:items-center sm:justify-between border border-blue-100 bg-white">
                    <div>
                      <h2 class="text-xl font-bold text-gray-800">اشتراک فعلی: 
                        <span v-if="Sub.level==1">رایگان</span>
                        <span v-if="Sub.level==2">نقره ای</span>
                        <span v-if="Sub.level==3">طلایی</span>
                      </h2>
                      <p class="text-sm text-gray-500 mt-1"> تاریخ آخرین خرید   :  
                        <span v-text="toPersianNumber(convertToJalali(Sub.startedAt))"></span>
                      </p>
                    </div>
                    <div class="flex items-center gap-3 mt-4 sm:mt-0">
                      <div v-if="Sub.isActive" class="text-sm bg-blue-100 text-blue-800 px-4 py-2 rounded-md font-medium">
                        <span v-text="toPersianNumber(Sub.remainingDays)"></span>
                        روز باقی‌مانده
                      </div>
                      <router-link :to="{name:'sub'}" v-show="Sub.level<3 && Sub.isActive"  class="text-sm bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-all">
                        ارتقا اشتراک
                      </router-link> 
                      <router-link to="{name:'sub'}" v-show="Sub.isActive==0"  class="text-sm bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-all">
                        ارتقا اشتراک
                      </router-link> 
                    </div>
                  </div>
              
                  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              
                    <div class="bg-white p-5 rounded-xl shadow border space-y-3">
  <div class="flex items-center gap-3">
    <div class="p-2 bg-blue-100 text-blue-600 rounded-md">
      <svg
        class="w-6 h-6"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path d="M3 7v13h18V7H3zm0-4h18v4H3V3z" />
      </svg>
    </div>
    <h3 class="text-lg font-semibold text-gray-700">پروژه‌ها</h3>
  </div>
  <p class="text-sm text-gray-500">
    {{ toPersianNumber(Sub.countDetail.project) }} از
    <span v-if="Sub.limits.max_projects === 9999">∞</span>
<span v-else>{{ toPersianNumber(Sub.limits.max_projects) }}</span>
  </p>
  <div class="w-full h-2 bg-gray-200 rounded">
    <div 
      class="h-2 bg-blue-500 rounded"
      :style="{ width: projectPercent + '%' }"
    >{{  }}</div>
    <h2>
      {{  }}
    </h2>
  </div>
</div>
<div class="bg-white p-5 rounded-xl shadow border space-y-3">
  <div class="flex items-center gap-3">
    <div class="p-2 bg-green-100 text-green-600 rounded-md">
      <svg class="w-6 h-6" fill="none" stroke="currentColor"><path d="M5 13l4 4L19 7" /></svg>
    </div>
    <h3 class="text-lg font-semibold text-gray-700">تسک‌ها</h3>
  </div>
  <p class="text-sm text-gray-500">
  {{ 
    Sub.level === 3
      ? `${toPersianNumber(Sub.countDetail.task || 0)} از ∞`
      : `${toPersianNumber(Sub.countDetail.task || 0)} از ${toPersianNumber(Sub.limits.max_tasks_per_project)}`
  }}
</p>
  <div class="w-full h-2 bg-gray-200 rounded">
    <div class="h-2 bg-green-500 rounded" :style="{ width: taskPercent.toFixed(0) + '%' }"></div>
  </div>
</div>
              
                    <div class="bg-white p-5 rounded-xl shadow border space-y-3">
  <div class="flex items-center gap-3">
    <div class="p-2 bg-purple-100 text-purple-600 rounded-md">
      <svg
        class="w-6 h-6"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path
          d="M17 20h5v-2a4 4 0 00-4-4h-1M9 20H4v-2a4 4 0 014-4h1m4-4a4 4 0 100-8 4 4 0 000 8zm6 4a4 4 0 10-8 0 4 4 0 008 0z"
        />
      </svg>
    </div>
    <h3 class="text-lg font-semibold text-gray-700">کاربران</h3>
  </div>
  
    <p class="text-sm text-gray-500">
  {{ toPersianNumber(Sub.countDetail.user) }} از
  {{ toPersianNumber(totalUserLimit) }} کاربر مجاز
  ({{ toPersianNumber(Sub.countDetail.project) }} پروژه ×
  {{ toPersianNumber(usersPerProject) }})
</p>

  <div class="w-full h-2 bg-purple-500/20 rounded">
    <div
      class="h-2 bg-purple-500 rounded"
      :style="{ width: userPercent + '%' }"
    ></div>
  </div>
</div>

              
                    <div class="bg-white p-5 rounded-xl shadow border flex items-center justify-between">
                      <div class="flex items-center gap-3">
                        <div class="p-2 bg-yellow-100 text-yellow-600 rounded-md">
                          <svg class="w-6 h-6" fill="none" stroke="currentColor"><path d="M9.75 17L4.75 12l5-5m5 10l5-5-5-5" /></svg>
                        </div>
                        <h3 class="text-base font-semibold text-gray-700">مانیتورینگ</h3>
                      </div>
                      
                      <span class="text-sm bg-green-100 text-green-700 px-2 py-1 rounded-full">فعال</span>
                    </div>
                    <div class="bg-white p-5 rounded-xl shadow border flex items-center justify-between">
                      <div class="flex items-center gap-3">
                        <div style="padding: 0.5rem; background-color: #bfdbfe; color: #2563eb; border-radius: 0.375rem;">

                                      <svg 
              class="w-6 h-6" 
              fill="none" 
              stroke="currentColor" 
              viewBox="0 0 24 24" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round"
            >
              <path d="M18 8a6 6 0 00-12 0c0 7-3 9-3 9h18s-3-2-3-9" />
              <path d="M13.73 21a2 2 0 01-3.46 0" />
      </svg>
                        </div>
                        <h3 class="text-base font-semibold text-gray-700">نوتفیکیشن</h3>
                      </div>
                      
                      <button v-if="!Sub.Permissions.notification" disabled class="text-sm bg-red-100 text-red-700 px-3 py-1 rounded-md cursor-not-allowed">
                        غیرفعال
                      </button>
                      <span v-else class="text-sm bg-green-100 text-green-700 px-2 py-1 rounded-full">فعال</span>
                    </div>
                    <div class="bg-white p-5 rounded-xl shadow border flex items-center justify-between">
                      <div class="flex items-center gap-3">
                        <div class="p-2 bg-cyan-100 text-cyan-600 rounded-md">
                          <svg class="w-6 h-6" fill="none" stroke="currentColor"><path d="M8 10h.01M12 10h.01M16 10h.01M9 16h6m-3-12a9 9 0 100 18 9 9 0 000-18z" /></svg>
                        </div>
                        <h3 class="text-base font-semibold text-gray-700">پرسش و پاسخ</h3>
                      </div>
                      <button v-if="!Sub.Permissions.issuese" disabled class="text-sm bg-red-100 text-red-700 px-3 py-1 rounded-md cursor-not-allowed">
                        غیرفعال
                      </button>
                      <span v-else class="text-sm bg-green-100 text-green-700 px-2 py-1 rounded-full">فعال</span>
                    </div>
              
                    <div class="bg-white p-5 rounded-xl shadow border flex items-center justify-between">
                      <div class="flex items-center gap-3">
                        <div class="p-2 bg-red-100 text-red-600 rounded-md">
                          <svg class="w-6 h-6" fill="none" stroke="currentColor"><path d="M18.364 5.636a9 9 0 00-12.728 0M5.636 18.364a9 9 0 0012.728 0M9 9l6 6m-6 0l6-6" /></svg>
                        </div>
                        <h3 class="text-base font-semibold text-gray-700">پشتیبانی</h3>
                      </div>
                      <button v-if="!Sub.Permissions.support" disabled class="text-sm bg-red-100 text-red-700 px-3 py-1 rounded-md cursor-not-allowed">
                        غیرفعال
                      </button>
                      <span v-else class="text-sm bg-green-100 text-green-700 px-2 py-1 rounded-full">فعال</span>
                    </div>
              
                    <div class="bg-white p-5 rounded-xl shadow border flex items-center justify-between">
                      <div class="flex items-center gap-3">
                        <div class="p-2 bg-gray-100 text-gray-600 rounded-md">
                          <svg class="w-6 h-6" fill="none" stroke="currentColor"><path d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14m0 0v-4m0 4a2 2 0 01-2 2H5a2 2 0 01-2-2V9a2 2 0 012-2h8a2 2 0 012 2v5z" /></svg>
                        </div>
                        <h3 class="text-base font-semibold text-gray-600">کنفرانس ویدئویی</h3>
                      </div>
                      <button v-if="!Sub.Permissions.video" disabled class="text-sm bg-red-100 text-red-700 px-3 py-1 rounded-md cursor-not-allowed">
                        غیرفعال
                      </button>
                      <span v-else class="text-sm bg-green-100 text-green-700 px-2 py-1 rounded-full">فعال</span>
                    </div>
              
                  </div>
                </div>
              </div>
</template>
<script setup>
import JDate from 'jalali-date';

import { useAuthStore } from '@/stores/auth';
import { useSubStore } from '@/stores/SubStore';
import { onMounted } from 'vue';
import { ref } from 'vue';
const auth=useAuthStore()
const projectPercent = ref(0);
const userPercent = ref(0);
const totalUserLimit = ref(0);
const usersPerProject = ref(10); 
const taskPercent = ref(0);
const totalTaskLimit = ref(0);
const tasksPerProject = ref(10);
const Sub=useSubStore()
onMounted(async () => {
  await Sub.fetchSubscriptionStatus(auth.user.access);

  if (!Sub.countDetail || !Sub.limits) {
    console.error("Subscription data missing", Sub);
    return;
  }

  const projectCount = Sub.countDetail.project || 0;
  const userCount = Sub.countDetail.user || 0;
  const taskCount = Sub.countDetail.task || 0;

  if (Sub.level === 3) {
    tasksPerProject.value = 999999;
    totalTaskLimit.value = '∞';
    taskPercent.value = 25;  
  } else {
    const isUnlimitedTasksPerProject = Sub.limits.max_tasks_per_project === 9999;

    if (isUnlimitedTasksPerProject) {
      tasksPerProject.value = 50;
    } else if (Sub.limits.max_tasks_per_project) {
      tasksPerProject.value = Sub.limits.max_tasks_per_project;
    }

    const totalTaskLimitCalculated = tasksPerProject.value;

    totalTaskLimit.value = totalTaskLimitCalculated;
    taskPercent.value = totalTaskLimitCalculated
      ? (taskCount / totalTaskLimitCalculated) * 100
      : 0;
  }

  const isUnlimitedProjects = Sub.limits.max_projects === 9999;
  const isUnlimitedUsersPerProject = Sub.limits.max_users_per_project === 9999;

  projectPercent.value = isUnlimitedProjects
    ? 10
    : (projectCount / Sub.limits.max_projects) * 100;

  if (isUnlimitedUsersPerProject) {
    usersPerProject.value = 50;
  } else if (Sub.limits.max_users_per_project) {
    usersPerProject.value = Sub.limits.max_users_per_project;
  }

  const totalUserLimitCalculated = usersPerProject.value;

  userPercent.value = totalUserLimitCalculated
    ? (userCount / totalUserLimitCalculated) * 100
    : 0;

  totalUserLimit.value = totalUserLimitCalculated;
});



function toPersianNumber(input) {
  const enToFaDigits = {
    "0": "۰", "1": "۱", "2": "۲", "3": "۳", "4": "۴",
    "5": "۵", "6": "۶", "7": "۷", "8": "۸", "9": "۹",
  };
  return String(input).replace(/\d/g, d => enToFaDigits[d] || d);
}

function convertToJalali(isoDate) {
  const date = new Date(isoDate);
  date.setTime(date.getTime() - 86400000);
  const jDate = new JDate(date);
  return `${jDate.getFullYear()}/${String(jDate.getMonth()).padStart(2, '0')}/${String(jDate.getDate()).padStart(2, '0')}`;
}
</script>
