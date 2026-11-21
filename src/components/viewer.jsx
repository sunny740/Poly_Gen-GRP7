import { Canvas, useLoader } from '@react-three/fiber'
import { OrbitControls, Center } from '@react-three/drei'
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js'
function Model({ url }) {
const obj = useLoader(OBJLoader, url)
return <Center><primitive object={obj} /></Center>
}
export default function Viewer({ url }) {
return (
<Canvas camera={{ position: [0, 1, 3], fov: 45 }}>
<ambientLight intensity={0.6} />
<directionalLight position={[3, 5, 2]} intensity={1.5} />
<Model url={url} />
<OrbitControls />
</Canvas>
)
}
