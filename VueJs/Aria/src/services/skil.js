
import axios from "@/utils/axios";


const createSkill=(token,info)=>{

    
    return axios.post("/workspace/create-skill/",{
        "name": info.name,
        "description": info.description
    } ,  {
        headers: {
            Authorization: `JWT ${token}`,
         
        }
    })
}
const getSkils=(token)=>{

    
    return axios.get("/workspace/create-skill/", {
        headers: {
            Authorization: `JWT ${token}`,
          
        }
    })
}

const deleteSkill=(token,id)=>{
    return axios.delete(`/workspace/create-skill/${id}/` ,  {
        headers: {
            Authorization: `JWT ${token}`,
          
        }
    })
}
const getSkill=(token,id)=>{
    return axios.get(`/workspace/create-skill/${id}/` , {
        headers: {
            Authorization: `JWT ${token}`,
          
        }
    })
}
const editskill=(token,id,info)=>{
    return axios.put(`/workspace/create-skill/${id}/` ,{
        'id':id,
        'name':info.name,
        'description':info.description
    },  {
        headers: {
            Authorization: `JWT ${token}`,
          
        }
    })
}
export {createSkill,getSkils,deleteSkill,getSkill,editskill}