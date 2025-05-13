import numpy as np
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

cap = cv2.VideoCapture(0)
counter = 0 
stage = None
prev_stage = None

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue
            
        frame = cv2.flip(frame, 1)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get coordinates for both arms
            shoulder_l = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow_l = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist_l = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
            shoulder_r = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow_r = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist_r = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            hip_r = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            hip_l = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            
            # Calculate angles
            angle_l = calculate_angle(shoulder_l, elbow_l, wrist_l)
            angle_r = calculate_angle(shoulder_r, elbow_r, wrist_r)
            shoulder_angle_l = calculate_angle(elbow_l, shoulder_l, 
                                             [shoulder_l[0], shoulder_l[1]-0.1])  # Vertical reference
            shoulder_angle_r = calculate_angle(elbow_r, shoulder_r, 
                                             [shoulder_r[0], shoulder_r[1]-0.1])  # Vertical reference
            angle_hl = calculate_angle(hip_l,shoulder_l,elbow_l)
            angle_hr = calculate_angle(hip_r,shoulder_r,elbow_r)
            
            # Improved counter logic
            prev_stage = stage
            
            if (angle_hl > 90 and angle_hr > 90):
                # Arms are down
                # if stage != "down":  # Only update if changing state
                stage = "down"
                can_count = True  # Reset the counting flag when we reach down position
                    
            else:
                stage ="move elbow"
            
            # Check if arms are in down position (elbows below shoulders and angles < 90)
            if angle_l < 90 and angle_r < 90 :
                stage = "down"
            
            # Check if arms are in up position (elbows above shoulders and angles > 160)
            elif angle_l > 160 and angle_r > 160 :
                stage = "up"
                
                # Only count if transitioning from down to up
                if prev_stage == "down":
                    counter += 1
                    print(f"Rep #{counter} completed!")
            
            # else:
                # stage = "moving"
                
        except Exception as e:
            print(f"Error: {e}")
            pass

        # Draw landmarks
        mp_drawing.draw_landmarks(
        image, 
        results.pose_landmarks, 
        mp_pose.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),  # Landmark spec
        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)   # Connection spec
)

        # Display info
        cv2.rectangle(image, (0,0), (235,90), (0,0,0), -1)
        cv2.putText(image, 'REPS', (15,35), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,255), 1)
        cv2.putText(image, str(counter), (15,70), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,255,255), 2)
        cv2.putText(image, 'STAGE', (100,35), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,255), 1)
        cv2.putText(image, stage, (100,70), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,255,255), 2)

        cv2.imshow('Shoulder Press Counter', image)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()