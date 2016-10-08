//
//  File.swift
//  Critic
//
//  Created by Christian Bueche on 10/8/16.
//  Copyright © 2016 Christian Bueche. All rights reserved.
//

import Foundation

var adjectives = ["subjuntive", "derivative", "subtle", "muted", "elongated", "intimate", "angular", "vibrant",
                  "earthy", "subtle", "saturated", "sublime"]

class Critique {
    
    //MARK: Properties
    var num_tags: Int
    var tags: [String]
    var sentence: String
    
    //MARK: Member Functions
    func critiqueIt(){
        if(num_tags == 0){
            sentence = "This piece is truly beyond any discrete definition.  It subverts expectation by defying our desire to analyze or quantify its formal elements."
        }
        if(num_tags == 1){
            sentence = "The use of" + tags[0] + "as subject matter here is interesting from an art historical perspective, but I feel that it lacks cohesion as a whole."
        }
        if(num_tags == 2){
            sentence = "It appears the artist was grappling with deep-seated feelings about" + tags[0] + "and" + tags[1] + ", searching for common thematic ground.  However, I find the lack of material exploration disappointing."
        }
        if(num_tags == 3){
            sentence = "" + tags[0] + "," + tags[1] + ", and" + tags[2] + ". These themes are so played out, its not even worth commenting on."
        }
        if(num_tags == 4){
            sentence = "Notice how the" + tags[0] + "is juxtaposed with the" + tags[1] + ", and further contrasted by the" + tags[2] + ". Its obvious that the artist is creating a conceptual foil for the" + tags[3] + "."
        }
        if(num_tags == 5){
            sentence = "The masterfully rendered" + tags[0] + "speaks of the artist's devotion to the medium. " + tags[1] + ", in combination with the" + tags[2] + ", create an atmosphere of adjective that is compunded by the rhythmic placement of" + tags[3] + "and" + tags[4] + "."
        }
        if(num_tags == 6){
            sentence = "Notice how the" + tags[0] + "is juxtaposed with the" + tags[1] + ", and further contrasted by the" + tags[2] + ". Its obvious that the artist is creating a conceptual foil for the" + tags[3] + "."
        }
        
    }
    
    //MARK: Initialization
    init?(num_tags: Int, tags: [String]){
        
        //Initialize properties
        self.num_tags = num_tags
        self.tags = tags
        self.sentence = "";
        
        // Initialization should fail if num_tags is negative.
        if num_tags < 0{
            return nil
        }
        
    }

    
}



