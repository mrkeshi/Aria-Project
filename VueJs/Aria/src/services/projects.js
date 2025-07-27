import axios from "@/utils/axios";

const getProjects=(token)=>{
return axios.get("http://127.0.0.1:8000/workspace/project/",{
    headers: {
        Authorization: `JWT ${token}`
    }
})
}
const setProject=(title,description,token)=>{
  

    return axios.post("http://127.0.0.1:8000/workspace/project/",{
        'title':title,
        'description':description,
        "status": false
    },{
        headers: {
            Authorization: `JWT ${token}`
        }
    })
    }

const editProject=(title,description,token,id)=>{
           
        return axios.put(`http://127.0.0.1:8000/workspace/project/${id}/`,{
            'title':title,
            'description':description,
            'status':false,
            
        },{
            headers: {
                Authorization: `JWT ${token}`
            }
        })
        }
        const singleProject=(token,id)=>{
    
            return axios.get(`http://127.0.0.1:8000/workspace/project/${id}`,{
                headers: {
                    Authorization: `JWT ${token}`
                }
            })
            }
            const setCurrentProject=(token,id)=>{
    
                return axios.get(`workspace/project/set-current-project/?project_id=${id}`,{
                    headers: {
                        Authorization: `JWT ${token}`
                    }
                })
                }
                const deleteproj=(token,id)=>{
    
                    return axios.delete(`workspace/project/${id}/`,{
                        headers: {
                            Authorization: `JWT ${token}`
                        }
                    })
                    }
        const getUserInProject=(token,projectId,roleId)=>{
            return axios.get(`workspace/project/${projectId}/role/${roleId}`,{
                headers: {
                    Authorization: `JWT ${token}`
                }
            })
        }
        const UpdateRole=(token,projectId,roleId,info)=>{
            return axios.put(`workspace/project/${projectId}/role/${roleId}/`,{
                "id": roleId,
                "skill": info.skill,
                "project": projectId,
                "level": info.level,
            },{
                headers: {
                    Authorization: `JWT ${token}`
                }
            })
        }
export {setProject,UpdateRole,getUserInProject,editProject,getProjects,singleProject,setCurrentProject,deleteproj}