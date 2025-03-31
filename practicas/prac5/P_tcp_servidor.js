const net = require('net'); 
 
const server = net.createServer();  

server.on('connection', (socket)=>{     
    socket.on('data', (data)=>{         
        console.log('\nEl cliente ' + socket.remoteAddress + ":" + 
            socket.remotePort + "dice: " + data);         
            socket.write('Mensaje recibido');     
        });      
        
    socket.on('close', ()=>{         
        console.log('Comunicación finalizada');
    }
    );

    socket.on('error', (err)=>{         
        console.log('Error en la comunicación: ' + err);     
    });
}
);

server.listen(8080, () => {
    console.log('Servidor TCP escuchando en el puerto 8080', server.address().port);
})
