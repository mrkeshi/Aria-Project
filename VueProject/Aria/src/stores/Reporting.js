import { defineStore } from "pinia";
import { useToast } from "vue-toastification";
import { useAuthStore } from "./auth";
import { createSkill, deleteSkill, editskill } from "@/services/skil";
import router from "@/router";
import { getDetailSerivce, getTaskAgo, getTopUserService } from "@/services/ReportService";
import JDate from 'jalali-date';
import jdate from "jalali-date";
export const useReportStore = defineStore({
    id: 'report',
    state: () => ({
        detailProject: {
            developers_of_project:0,
            project_task_count:0,
            user_projects:1,
            questions:0
        },
        topuser:[{}],
        returnUrl: null,
        task:[]
    }),
    computed:{
     
    },
    actions: {
        convertToShamsi(dateString) {
            const date = new Date(dateString);

            const jDate = new JDate(date);
            const shamsiMonth = jDate.getMonth();
const shamsiDay = jDate.getDate();

return(`${shamsiMonth}/${shamsiDay}`);
          
        },
       async getDetail(token,id){
        await getDetailSerivce(token,id).then((result)=>{
            console.log(result)
            Object.assign(this.detailProject,result.data)
        }).catch((er)=>{
            console.log(er)
        })
       },

    
       async getTopUser(token,id){
        await getTopUserService(token,id).then((result)=>{
            Object.assign(this.topuser,result.data)
        })
       },

       async getTaskAgo(token){
        await getTaskAgo(token).then((res)=>{
            this.task=[]
          res.data.forEach(element => {

            this.task.push({
                count:element.count,
                date:this.convertToShamsi(element.date)
            })
        
          });
        })
       }
    },
   
});