import React,{Component}from 'react'
import './todo.css';
import axios from 'axios';


   


class Todo extends Component{
    constructor(props){
        super(props);
        this.state={
            item:[],
            textconts :"",
            desconts:""

        };
    };
    componentDidMount=()=>{axios.get('http://localhost:8000/todo')
.then(response=>this.setState({item:response.data})).catch(error=>console.log(error))
}
    
    additem=(e)=>{
       let items=this.state.item;
       items.push({'title':this.state.textconts,'description':this.state.desconts});
       //this.setState({item:items})
        axios.post('http://localhost:8000/todo_id',{'title':this.state.textconts,'description':this.state.desconts})
        .then(response=>this.setState({item:items}))
        .catch(error=>console.log(error))
    }
    removeconts=(key,k)=>{
        if(!window.confirm("You sure wanna delete Current task ??"))
        {
            return;
        }
        let currentitems=this.state.item;
        currentitems.splice(key,1);
        this.setState({item:currentitems})
        axios.delete(`http://localhost:8000/todo_delete/${k}`)
        .then(response=>alert(response.data))
        .catch(error=>console.log(error))
        
        
    }
    render(){

        return(
        <div className="todo-name">
            {console.log(this.state.item)}
            <form className="input-txt">
            <h1>TodoApp</h1>
            <input type='text'placeholder="Title" onChange={(e)=>
             this.setState({textconts:e.target.value})}/>
             <input type='text' placeholder="Description"onChange={(e)=>
              this.setState({desconts:e.target.value})}/>
            <button onClick={this.additem}>Add Todo</button>
            </form>
        <ul>

    <h3>Current Tasks</h3>

    {this.state.item.map((itm,key)=>{
    return(
    <li>{itm.title}:- {itm.description}   <i className="fas fa-trash"onClick={()=>{this.removeconts(key,itm.title)}}></i></li>
)
})}

</ul>
                

          

        </div>


        );
}

}
export default Todo;