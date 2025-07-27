<template>
 <jalaliCalendar
  :eventsList="events"
  :vacationsList="vacations"
  disablePastDays
  @dayClick="showEventModal"
  @on-event-click="showEventModal"
/>

  </template>
  
  <script setup lang="ts">
  import { ref, onMounted, nextTick } from "vue";
  import { jalaliCalendar } from "vue3-jalali-calendar";
  import { useRouter } from "vue-router";
  import moment from "jalali-moment";
  import { useTaskStore } from "@/stores/TaskStore";
  
  const taskStore = useTaskStore();
  const router = useRouter();
  const events = ref([]);
  const vacations = ref([]);
  
  function getColorByImportance(importance: number) {
    if (importance == 1) return "#ef4444";
    if (importance == 2) return "#f59e0b";
    if (importance == 3) return "#10b981";
    return "#6b7280";
  }
  
  function showEventModal(e: any) {
    if (e.dwa) {
      router.push({ name: "singletask", params: { id: e.dwa } });
    }
  }
  
  function mapTasksToEvents(tasks: any[]) {
    return tasks
      .filter((task) => task.created_at && task.finished_at && task.progress < 100)
      .map((task) => ({
        dwa: task.id,
        startDateTime: moment(task.created_at),
        endDateTime: moment(task.finished_at),
        title: task.title || "بدون عنوان",
        color: getColorByImportance(task.importance),
      }));
  }
  
  function toPersianNumbers(str = "") {
    const map = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];
    return str.replace(/\d/g, (d) => map[+d]);
  }
  
  function convertNumbersInElement(element: HTMLElement) {
    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
      node.textContent = toPersianNumbers(node.textContent || "");
    }
  }
  
  onMounted(async () => {
    await taskStore.ShowallTaskAction();
    events.value = mapTasksToEvents(taskStore.tasks);
  
    nextTick(() => {
      const root = document.querySelector(".vpc_root") as HTMLElement | null;
      if (!root) return;
  
      convertNumbersInElement(root);
  
      const eventBoxes = document.querySelectorAll(".vpc_event");
      eventBoxes.forEach((el, i) => {
        if (events.value[i]) {
          (el as HTMLElement).style.backgroundColor = events.value[i].color;
          (el as HTMLElement).style.fontSize = "1.2rem";
        }
      });
  
      const buttons = document.querySelectorAll(".vpc_period-btn");
      buttons.forEach((button) => {
        button.addEventListener("click", () => {
          router.push({ name: "addtask" });
        });
      });
  
      setInterval(() => {
        convertNumbersInElement(root);
      }, 2000);
    });
  });
  </script>
  
  <style>
  .vpc_event {
    font-size: 1.2rem !important;
    font-weight: 400;
    color: white;
  }
  @media (max-width: 768px) {
    #vpc_date-control {
      display: none !important;
    }
  }
  </style>
  