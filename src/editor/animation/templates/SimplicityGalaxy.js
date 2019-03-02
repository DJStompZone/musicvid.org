

import OrthographicScene from '../common/scenes/OrthographicScene'
import WebGLManager from '../WebGLManager'

export default class Manager extends WebGLManager {

    setUpScene() {
        const scene = new OrthographicScene(this.layersFolder, this.resolution);
        

        const it0 = scene.addItemFromText("SimplicityGalaxy");
        const it1 = scene.addItemFromText("SpriteTextMask");
        it0.setUpGUI(this.overviewFolder, "SimplicityGalaxy");
        it1.setUpGUI(this.overviewFolder, "Overlay");
        this.overviewFolder.onResize();
        this.scenes.push(scene);
    }

}