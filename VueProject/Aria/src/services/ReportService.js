
import axios from "@/utils/axios";



const getDetailSerivce=(token,id)=>{

    
    return axios.get(`reporting/ProjectDetail/${id}/`, {
        headers: {
            Authorization: `JWT ${token}`,
          
        }
    })
}
const getTaskStatus=(token)=>{
return axios.get('reporting/ReportingTasksResult/',{
    headers: {
        Authorization: `JWT ${token}`,
      
    } 
})
}
const getCategory=(token)=>{
    return axios.get('reporting/CountOfTaskByEachTask/',{
        headers: {
            Authorization: `JWT ${token}`,
          
        } 
    })
    }
    const getTopUserService=(token,id)=>{

    
        return axios.get(`reporting/TopUserInProject/${id}/`, {
            headers: {
                Authorization: `JWT ${token}`,
              
            }
        })
    }
    const getTaskAgo=(token)=>{

    
        return axios.get(`reporting/CompletedTaskIn10DaysAgo/`, {
            headers: {
                Authorization: `JWT ${token}`,
              
            }
        })
    }
export {getDetailSerivce,getTaskStatus,getCategory,getTopUserService,getTaskAgo}