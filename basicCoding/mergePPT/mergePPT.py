# spire.presentation is not license free and resources are limitated
from spire.presentation import *
from spire.presentation.common import *

# Create two instances of Presentation class
pres1 = Presentation()
pres2 = Presentation()

# Load two presentation files
pres1.LoadFromFile("first_presentation.pptx")
pres2.LoadFromFile("second_presentation.pptx")
 
# Iterate through the slides of the second presentation
for slide in pres2.Slides:
    # Add each slides to the first presentation and keep the original design
    pres1.Slides.AppendBySlide(slide)

# Save the first presentation
pres1.SaveToFile("MergePresentations.pptx", FileFormat.Pptx2016)
pres1.Dispose()
pres2.Dispose()
