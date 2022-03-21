import React,{ useState } from 'react';
import APIService from '../Components/APIService'


const TempForm = (props) => {
    const [test, setText] = useState('')
    // const test = ""

    const getParms = () =>{
      APIService.GetParms(test)
      .then((response) => props.test(response))
      .catch(error => console.log('error',error))
    }

    const handleSubmit2=(event)=>{ 
      event.preventDefault()   
      getParms()
    //   setText('')
    }

  return (
    <div className="shadow p-4">

        <form onSubmit = {handleSubmit2} >

          <label htmlFor="title" className="form-label">Enter Text</label>
          <input 
          type="text"
          className="form-control" 
          placeholder ="Enter title"
          value={test}
          onChange={(e)=>setText(e.target.value)}
          required
          />

          <button 
          className="btn btn-primary mt-2"
          >
          Submit</button>
          
        </form>

    </div>
  )}

export default TempForm;