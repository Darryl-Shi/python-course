import rocket as rocket_module

rocket = rocket_module.Rocket()
print("The rocket is at (%d, %d)." % (rocket.x, rocket.y))

shuttle = rocket_module.Shuttle()
print("\nThe shuttle is at (%d, %d)." % (shuttle.x, shuttle.y))
print("The shuttle has completed %d flights." % shuttle.flights_completed)