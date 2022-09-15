import React, { useEffect, useState } from "react";
import { generateGraph } from "../../service/api";
import "./styles.css"

export default function Board() {
  const [image, setImage] = useState(null);

  const handleSubmit = async () => {
    var nodes_number = document.querySelector("#node-number").value;
    // console.log(nodes_number)
    var max_time = document.querySelector("#max-time").value;
    // console.log(max_time)
    var leave_nodes = document.querySelector("#leave-nodes").value;
    // console.log(leave_nodes.split(", "))
    var arrive_nodes = document.querySelector("#arrive-nodes").value;
    // console.log(arrive_nodes)
    var nodes_width = document.querySelector("#nodes-width").value;
    // console.log(nodes_width)
    try {
      const sendObj = {
        "nodes_number": nodes_number,
        "max_time": max_time,
        "leave_nodes": leave_nodes.split(", "),
        "arrive_nodes": arrive_nodes.split(", "),
        "nodes_width": nodes_width.split(", ")
      }    
      const graph = await generateGraph(sendObj)
      setImage(graph.data.image_string)
    } catch (error) {
      alert("Não foi possível gerar a jornada, verifique se preencheu corretamente!")
    }
  }

  const onReset = () => {
    setImage(null)
  }

  return (
    <div className='board'>
          {image ? 
          <>
            <h1 className="header-h1 blue">A jornada ideal é:</h1>
            <img src={`data:image/png;base64,` + image} alt="graph"/>
            <button onClick={onReset} className='board-button-2'>Tentar novamente</button>
          </>
          :
            <>
              <div className='inline-flex'>
                <div className="board-span-input">
                  <span className='board-span'>Número do nó:</span>
                  <input id="node-number" className='board-input-1' placeholder='6'
                  />
                </div>
                <div className="board-span-input">
                  <span className='board-span'>Tempo máximo:</span>
                  <input id="max-time" className='board-input-1' placeholder='7'
                  />
                </div>
              </div>
              <div className='inline-flex'>
                <div className="board-span-input">
                  <span className='board-span'>Origens:</span>
                  <textarea id="leave-nodes" className='board-text-area' cols="2" placeholder="1, 1, 3, 2, 4, 6"></textarea>
                </div>
                <div className="board-span-input">
                  <span className='board-span'>Destinos:</span>
                  <textarea id="arrive-nodes" className='board-text-area' cols="2" placeholder="2, 3, 6, 4, 6, 5"></textarea>
                </div>
              </div>
              <span className='board-span'>Largura dos nós:</span>
              <textarea id="nodes-width" className='board-text-area' cols="2" placeholder="2, 3, 3, 2, 2, 1"></textarea>
              <button onClick={handleSubmit} type='submit' className='board-button'>Traçar jornada</button>
            </>
          }
    </div>
  );
}